# machine_learning_medical_data_workshop

## JupyterLite op GitHub Pages

Deze repository bevat een JupyterLite-setup voor de workshop notebook.

### Wat is toegevoegd

- Workflow: `.github/workflows/deploy-jupyterlite.yml`
- Config: `jupyter_lite_config.json`

### Eenmalig instellen in GitHub

1. Open je repository op GitHub.
2. Ga naar **Settings > Pages**.
3. Kies bij **Build and deployment**: **Source = GitHub Actions**.

### Deployen

1. Push naar `main` (of `master`).
2. De workflow bouwt JupyterLite en publiceert naar GitHub Pages.
3. Je site staat daarna op:
	`https://<jouw-gebruikersnaam>.github.io/machine_learning_medical_data_workshop/`

### Inhoud van de JupyterLite build

De build neemt standaard deze bestanden mee:

- `workshop_convolutie_geen_ai_jupyterlite.ipynb`
- `workshop_utils.py`
- `chess.jpg`
- `woman.jpg`

Pas dit aan in `jupyter_lite_config.json` als je meer notebooks of assets wilt tonen.

