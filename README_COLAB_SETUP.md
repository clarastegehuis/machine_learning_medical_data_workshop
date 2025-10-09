# 🎨 Convolutie Workshop - Setup Instructies

## 📁 Bestanden in deze workshop:
- `workshop_convolutie_geen_ai.ipynb` - Hoofdnotebook voor leerlingen
- `workshop_utils.py` - Technische functies (automatisch geladen)
- `README.md` - Deze instructies

## 🌍 Ondersteunde Platforms
Deze workshop werkt op:
- ✅ **Google Colab** - Automatische file upload
- ✅ **Lokaal Jupyter** - Handmatige file methoden

## 🌐 Google Colab Setup

### Stap 1: GitHub Repository
1. **Upload beide bestanden** naar je GitHub repository
2. **Zorg dat ze in dezelfde directory staan**

### Stap 2: Colab Badge aanpassen
In de notebook, verander deze regel in cel 1:
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JOUW_USERNAME/JOUW_REPO/blob/main/workshop_convolutie_geen_ai.ipynb)
```

### Stap 3: GitHub URL aanpassen  
In cel 7, verander deze regel:
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

## 💻 Lokale Setup

### Vereisten:
```bash
pip install numpy matplotlib torch Pillow jupyter
```

### Foto Upload Opties:
1. **Google Colab**: Automatische upload widget
2. **Lokaal**: Gebruik `load_alternative_image('filename.jpg')`
3. **Handmatig**: Zet foto in dezelfde map als notebook

## 🔧 Troubleshooting

### ❌ "Module niet gevonden" error in Colab:
- Controleer of `workshop_utils.py` in je repository staat
- Controleer of de GitHub URLs kloppen
- De backup functies zouden automatisch moeten laden

### ❌ Download faalt in Colab:
- Controleer internetverbinding
- Repository moet publiek zijn
- GitHub URLs moeten naar 'raw' content wijzen

### ❌ Foto upload werkt niet lokaal:
- Gebruik `load_alternative_image('filename.jpg')` direct
- Zet foto in dezelfde map als notebook
- Controleer bestandsnaam en extensie (.jpg, .png, .jpeg)

### ❌ Import errors lokaal:
- Installeer ontbrekende packages: `pip install package_name`
- Controleer Python versie (>= 3.7 aanbevolen)
- Herstart kernel na package installaties