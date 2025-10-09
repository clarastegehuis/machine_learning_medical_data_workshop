# 🎨 Convolutie Workshop - Setup Instructies

## 📁 Bestanden in deze workshop:
- `workshop_convolutie_geen_ai.ipynb` - Hoofdnotebook voor leerlingen
- `workshop_utils.py` - Technische functies (automatisch geladen)
- `README.md` - Deze instructies

## � Ondersteunde Platforms
Deze workshop werkt op:
- ✅ **Google Colab** - Automatische file upload
- ✅ **JupyterHub** - Upload widget met ipywidgets  
- ✅ **JupyterLab** - Upload widget met ipywidgets
- ✅ **Lokaal Jupyter** - Handmatige file methoden

## �🌐 Google Colab Setup

### Stap 1: GitHub Repository
1. **Upload beide bestanden** naar je GitHub repository
2. **Zorg dat ze in dezelfde directory staan**

### Stap 2: Colab Badge aanpassen
In de notebook, verander deze regel in cel 1:
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JOUW_USERNAME/JOUW_REPO/blob/main/workshop_convolutie_geen_ai.ipynb)
```

### Stap 3: GitHub URL aanpassen  
In cel 6, verander deze regel:
```python
utils_url = "https://raw.githubusercontent.com/JOUW_USERNAME/JOUW_REPO/main/workshop_utils.py"
```

## 🧪 Testen

### Lokaal testen:
```bash
jupyter notebook workshop_convolutie_geen_ai.ipynb
```

### Google Colab testen:
1. Ga naar je GitHub repository
2. Klik op de "Open in Colab" badge
3. Voer de eerste cellen uit
4. Controleer of `workshop_utils.py` wordt gedownload

## �️ JupyterHub/JupyterLab Setup

### Vereisten:
- `ipywidgets` geïnstalleerd voor upload functionaliteit
- Anders valt het terug op handmatige file upload

### Foto Upload Opties:
1. **Automatisch**: Upload widget verschijnt bij `upload_and_process_image()`
2. **Handmatig**: Sleep bestanden naar file browser
3. **Directe load**: Gebruik `load_alternative_image('filename.jpg')`

### Installatie ipywidgets (indien nodig):
```bash
pip install ipywidgets
# Of in notebook cel:
!pip install ipywidgets
```

## �🔧 Troubleshooting

### ❌ "Module niet gevonden" error in Colab:
- Controleer of `workshop_utils.py` in je repository staat
- Controleer of de GitHub URLs kloppen
- De backup functies zouden automatisch moeten laden

### ❌ Download faalt in Colab:
- Controleer internetverbinding
- Repository moet publiek zijn
- GitHub URLs moeten naar 'raw' content wijzen

### ❌ Upload widget werkt niet in JupyterHub/Lab:
- Installeer ipywidgets: `pip install ipywidgets`
- Herstart de kernel na installatie
- Gebruik handmatige upload als alternatief

### ❌ Foto upload timeout in JupyterHub/Lab:
- Probeer kleinere foto's (<5MB)
- Gebruik `load_alternative_image('filename.jpg')` direct
- Sleep foto naar file browser en herstart upload cel

### ❌ Import errors:
- Zorg dat beide bestanden in dezelfde directory staan
- Herstart de Colab runtime: Runtime → Restart runtime

## 🎯 Voor Docenten

### Classroom Setup:
1. **Fork deze repository** naar je eigen GitHub account
2. **Pas de URLs aan** naar je eigen repository  
3. **Deel de Colab link** met leerlingen
4. **Test eerst zelf** voordat je het uitzet

### Aanpassingen maken:
- **Technische functies**: Edit `workshop_utils.py`
- **Workshop inhoud**: Edit `workshop_convolutie_geen_ai.ipynb`
- **Beide bestanden** moeten gesynchroniseerd blijven

## 🚀 Deployment opties

### Optie 1: GitHub + Colab (Aanbevolen)
- ✅ Gratis hosting
- ✅ Automatische updates
- ✅ Makkelijk delen
- ✅ Version control

### Optie 2: Lokaal Jupyter
- ✅ Volledige controle
- ✅ Offline werken
- ❌ Moeilijker distribution

### Optie 3: JupyterHub/Binder
- ✅ Custom environments
- ❌ Complexere setup
- ❌ Mogelijk hosting costs

## 📞 Support

Als je problemen hebt:
1. Check de troubleshooting sectie hierboven
2. Controleer of alle URLs kloppen
3. Test in een fresh Colab environment
4. Check de GitHub repository permissions

Happy teaching! 🎉