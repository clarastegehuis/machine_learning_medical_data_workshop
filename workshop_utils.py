# 🛠️ Workshop Utilities - Technische functies voor de convolutie workshop
# 
# Dit bestand bevat alle technische functies die leerlingen niet hoeven te zien
# Import deze functies met: from workshop_utils import *

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F
from PIL import Image
from IPython.display import display, clear_output
import io
import base64

def open_img(path):
    """Open een afbeelding van verschillende formaten"""
    try:
        if path.endswith('.png') or path.endswith('.jpg') or path.endswith('.jpeg'):
            return np.array(Image.open(path).convert('L'))
        elif path.endswith('.mhd'):
            import SimpleITK as sitk
            return sitk.GetArrayFromImage(sitk.ReadImage(path))[32,:,:]
    except:
        print(f"❌ Kon {path} niet openen")
        return None

def visualize(img, title="Afbeelding", clim=None):
    """Laat een afbeelding mooi zien"""
    plt.figure(figsize=(8, 6))
    if clim:
        plt.imshow(img, cmap='gray', clim=clim)
    else:
        plt.imshow(img, cmap='gray')
    plt.title(title, fontsize=14)
    plt.axis('off')
    plt.show()

def create_sample_image():
    """Maak een simpele testafbeelding als we geen andere hebben"""
    # Maak een simpel patroon
    img = np.zeros((100, 100))
    img[20:80, 20:40] = 255  # Witte rechthoek
    img[20:40, 60:80] = 255  # Nog een witte rechthoek
    img[60:80, 60:80] = 255  # En nog een
    # Voeg wat lijnen toe
    img[10, :] = 255  # Horizontale lijn
    img[:, 10] = 255  # Verticale lijn
    return img

def resize_image_smart(img, max_pixels=50000):
    """
    Verkleint afbeeldingen die te groot zijn voor snellere verwerking
    
    Parameters:
    - img: De originele afbeelding
    - max_pixels: Maximum aantal pixels (standaard 50.000 = ongeveer 224x224)
    
    Returns:
    - Verkleinde afbeelding
    """
    height, width = img.shape
    current_pixels = height * width
    
    if current_pixels <= max_pixels:
        print(f"📏 Afbeelding is al klein genoeg ({current_pixels:,} pixels)")
        return img
    
    # Bereken nieuwe afmetingen met behoud van aspect ratio
    scale_factor = np.sqrt(max_pixels / current_pixels)
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)
    
    # Gebruik PIL voor high-quality resizing
    pil_img = Image.fromarray(img.astype('uint8'))
    resized_pil = pil_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_img = np.array(resized_pil)
    
    print(f"📏 Afbeelding verkleind van {height}x{width} ({current_pixels:,} pixels)")
    print(f"   naar {new_height}x{new_width} ({new_height*new_width:,} pixels)")
    print(f"   💡 Dit maakt de filters {current_pixels/(new_height*new_width):.1f}x sneller!")
    
    return resized_img

def upload_and_process_image():
    """Upload een foto en zet hem om naar zwart-wit voor convolutie experimenten"""
    
    # Detect environment
    try:
        from google.colab import files
        IN_COLAB = True
        environment = "Google Colab"
    except ImportError:
        IN_COLAB = False
        # Check if we're in Binder or other Jupyter environment
        try:
            from IPython import get_ipython
            if get_ipython() and 'IPKernelApp' in get_ipython().config:
                # Check if we're specifically in Binder
                import os
                if 'BINDER_SERVICE_HOST' in os.environ or 'BINDER_URL' in os.environ:
                    environment = "Binder"
                else:
                    environment = "Jupyter (Local/Hub/Lab)"
            else:
                environment = "Local Python"
        except:
            environment = "Local Python"
    
    print(f"🌍 Environment detected: {environment}")
    
    if IN_COLAB:
        # Google Colab upload method
        print("📤 Klik op 'Choose Files' om je foto te uploaden...")
        uploaded = files.upload()
        
        if uploaded:
            filename = list(uploaded.keys())[0]
            return process_uploaded_file(uploaded[filename], filename)
        else:
            print("❌ Geen foto geüpload")
            return None
            
    elif environment == "Binder":
        # Binder environment with optimized upload
        print("🚀 Binder gedetecteerd - Upload widget wordt gestart...")
        
        try:
            import ipywidgets as widgets
            from IPython.display import display, clear_output
            import time
            
            # Create upload widget optimized for Binder
            upload_widget = widgets.FileUpload(
                accept='image/*',  # Only accept image files
                multiple=False,
                description='📤 Upload Photo',
                style={'description_width': 'initial'},
                layout=widgets.Layout(width='320px')
            )
            
            print("📤 Gebruik de upload widget hieronder (Binder-optimized):")
            display(upload_widget)
            
            # Wait for upload with longer timeout for Binder
            print("⏳ Wachten op upload... (max 20 seconden)")
            for i in range(100):  # Wait up to 20 seconds for Binder
                if upload_widget.value:
                    uploaded_file = upload_widget.value[0]
                    filename = uploaded_file['metadata']['name']
                    file_content = uploaded_file['content']
                    
                    print(f"✅ Foto '{filename}' geüpload via Binder widget!")
                    return process_uploaded_file(file_content, filename)
                time.sleep(0.2)
            
            print("⏰ Upload timeout - probeer handmatige methode hieronder")
            return try_manual_upload()
            
        except ImportError:
            print("❌ ipywidgets niet beschikbaar in Binder!")
            print("💡 Zorg dat requirements.txt in je repository staat:")
            print("   - numpy>=1.21.0")
            print("   - matplotlib>=3.5.0") 
            print("   - torch>=1.12.0")
            print("   - Pillow>=8.3.0")
            print("   - ipywidgets>=7.6.0")
            print("🔄 Herstart Binder na toevoegen requirements.txt")
            return try_manual_upload()
    
    elif environment.startswith("Jupyter"):
        # Other Jupyter environments (Hub/Lab/Local)
        print("💻 Jupyter omgeving gedetecteerd - Upload widget beschikbaar...")
        
        try:
            import ipywidgets as widgets
            from IPython.display import display, clear_output
            import time
            
            # Create standard upload widget
            upload_widget = widgets.FileUpload(
                accept='image/*',
                multiple=False,
                description='Upload Image',
                style={'description_width': 'initial'},
                layout=widgets.Layout(width='300px')
            )
            
            print("📤 Gebruik de upload widget hieronder:")
            display(upload_widget)
            
            # Standard timeout for other Jupyter environments
            print("⏳ Wachten op upload... (max 15 seconden)")
            for i in range(75):
                if upload_widget.value:
                    uploaded_file = upload_widget.value[0]
                    filename = uploaded_file['metadata']['name']
                    file_content = uploaded_file['content']
                    
                    print(f"✅ Foto '{filename}' geüpload via Jupyter widget!")
                    return process_uploaded_file(file_content, filename)
                time.sleep(0.2)
            
            print("⏰ Upload timeout - probeer handmatige methode hieronder")
            return try_manual_upload()
            
        except ImportError:
            print("⚠️ ipywidgets niet beschikbaar - probeer handmatige upload")
            return try_manual_upload()
            
    else:
        # Local environment
        return try_manual_upload()

def process_uploaded_file(file_content, filename):
    """Process uploaded file content into grayscale image"""
    try:
        # Open en converteer naar zwart-wit
        img = Image.open(io.BytesIO(file_content))
        img_gray = np.array(img.convert('L'))
        
        print(f"🔄 Foto omgezet naar zwart-wit ({img_gray.shape[0]}x{img_gray.shape[1]} pixels)")
        
        # Verkleein de afbeelding voor betere performance
        img_gray = resize_image_smart(img_gray, max_pixels=50000)
        
        # Laat de originele en verwerkte versie zien
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        ax1.imshow(img)
        ax1.set_title("📸 Originele Foto")
        ax1.axis('off')
        
        ax2.imshow(img_gray, cmap='gray')
        ax2.set_title("⚫⚪ Zwart-Wit Versie (Verkleind)")
        ax2.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        return img_gray
        
    except Exception as e:
        print(f"❌ Fout bij verwerken foto: {e}")
        return None

def try_manual_upload():
    """Fallback method for manual file upload"""
    print("📁 Handmatige upload opties:")
    print("   1. 🖱️  Sleep een foto naar de file browser (links)")
    print("   2. 📂 Upload via menu: File → Upload Files") 
    print("   3. � Binder: Gebruik de Upload knop in de interface")
    print("   4. �💾 Zet een foto in dezelfde map als de notebook")
    print("   5. 🔄 Herstart deze cel nadat je een foto hebt toegevoegd")
    
    # Check for recently added files
    import os
    recent_images = []
    if os.path.exists('.'):
        for file in os.listdir('.'):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                recent_images.append(file)
    
    if recent_images:
        print(f"\n📸 Gevonden afbeeldingen in huidige map:")
        for i, img_file in enumerate(recent_images[:5]):  # Show max 5 files
            print(f"   {i+1}. {img_file}")
        
        print(f"\n💡 TIP: Gebruik load_alternative_image('bestandsnaam.jpg')")
    
    return None

def load_alternative_image(filename=None):
    """Laad een alternatieve afbeelding als uploaden niet werkt"""
    
    if filename:
        # Try specific filename
        img = open_img(filename)
        if img is not None:
            print(f"✅ Afbeelding geladen van: {filename}")
            img = resize_image_smart(img, max_pixels=50000)
            return img
        else:
            print(f"❌ Kon {filename} niet vinden")
    
    # Probeer een lokaal bestand (gebruikers kunnen dit aanpassen)
    local_paths = [
        "test_image.jpg",  # Vervang dit door een bestaand lokaal bestand
        "foto.jpg",  # Gebruikers kunnen hun foto hier neerzetten
        "image.png",
        # Voeg hier meer paden toe als nodig
    ]

    for path in local_paths:
        img = open_img(path)
        if img is not None:
            print(f"✅ Afbeelding geladen van: {path}")
            # Verkleien de afbeelding automatisch voor betere performance
            img = resize_image_smart(img, max_pixels=50000)
            return img
    
    # Als alles faalt, maak een testafbeelding
    print("🎨 Maken van een testafbeelding...")
    return create_sample_image()

def apply_conv(image, kernel, iter=1, title_prefix="Filter Effect"):
    """
    Past een convolutie toe op een afbeelding. Dit is de motor achter alle filters.
    
    Parameters:
    - image: De foto om te bewerken
    - kernel: Het "recept" voor het effect
    - iter: Hoe vaak het effect toegepast wordt
    - title_prefix: Naam van het effect
    """
    image, kernel = torch.from_numpy(image).float(), torch.from_numpy(kernel).float()
    img_shape, kernel_shape = image.shape, kernel.shape
    
    # Bepaal automatisch een goede clim op basis van de afbeelding
    original_min, original_max = image.min().item(), image.max().item()
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    print(f"⚡ {title_prefix} wordt toegepast...")
    print(f"   Kernel: {kernel_shape[0]}x{kernel_shape[1]}")
    print(f"   Iteraties: {iter}")
    
    for level in range(iter):
        # Pas convolutie toe
        image = F.conv2d(image.reshape(1, 1, img_shape[0], img_shape[1]),
                         kernel.reshape(1, 1, kernel_shape[0], kernel_shape[1]),
                         padding='same').squeeze()
        
        # Update de display
        ax.clear()
        ax.imshow(image.numpy(), cmap='gray', clim=[original_min, original_max])
        ax.set_title(f'⚡ {title_prefix} - Stap {level+1}/{iter}', fontsize=16)
        ax.axis('off')
        
        display(fig)
        clear_output(wait=True)
        plt.pause(0.2)
    
    plt.close()
    print(f"🎉 {title_prefix} voltooid!")
    
    if iter>1:
        # Laat het eindresultaat nog een keer zien
        final_result = image.numpy()
        visualize(final_result, f"Eindresultaat: {title_prefix}")
    
    return image.numpy()

def show_kernel(kernel, title="Kernel"):
    """Laat een kernel mooi zien"""
    plt.figure(figsize=(6, 4))
    plt.imshow(kernel, cmap='RdBu_r', interpolation='nearest')
    plt.title(f"🔧 {title}")
    plt.colorbar(label='Waarde')
    
    # Voeg getallen toe aan elke cel
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            plt.text(j, i, f'{kernel[i, j]:.1f}', 
                    ha='center', va='center', fontsize=12, fontweight='bold')
    plt.show()

def create_filter_gallery(image):
    """Laat alle filters naast elkaar zien - zoals een Instagram filter preview!"""
    
    print("🎨 Maken van filter gallery...")
    
    # Alle kernels definiëren
    kernels = {
        "Origineel": np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),  # Identity (geen verandering)
        "Blur": np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16,
        "Sharpen": np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
        "Vertical Edge": np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]]),
        "Horizontal Edge": np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
    }
    
    # Maak een 2x3 grid
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('🎨 Filtergalerij - Elk filter toegepast op het origineel', fontsize=16)
    
    for i, (name, kernel) in enumerate(kernels.items()):
        row, col = divmod(i, 3)
        
        # Pas filter toe
        if name == "Origineel":
            result = image
            # Gebruik originele image range voor normale weergave
            vmin, vmax = image.min(), image.max()
        else:
            # Maak elke keer een NIEUWE copy van de originele afbeelding
            image_tensor = torch.from_numpy(image.copy()).float()
            kernel_tensor = torch.from_numpy(kernel).float()
            result = F.conv2d(image_tensor.reshape(1, 1, *image_tensor.shape),
                            kernel_tensor.reshape(1, 1, *kernel.shape),
                            padding='same').squeeze().numpy()
            
            # Bepaal de juiste colormap range voor dit filter type
            if "Edge" in name or name == "Emboss":
                # Voor edge detection: gebruik symmetrische range rond 0
                abs_max = max(abs(result.min()), abs(result.max()))
                vmin, vmax = -abs_max * 0.3, abs_max * 0.3  # Verminder contrast voor betere zichtbaarheid
            else:
                # Voor andere filters: gebruik originele range
                vmin, vmax = image.min(), image.max()
        
        # Toon resultaat met aangepaste colormap
        axes[row, col].imshow(result, cmap='gray', vmin=vmin, vmax=vmax)
        axes[row, col].set_title(name, fontsize=12)
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Galerij voltooid!")

print("🛠️ Workshop utilities geladen! Alle technische functies zijn beschikbaar.")