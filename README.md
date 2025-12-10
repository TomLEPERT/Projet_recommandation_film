# Projet Python – Simplon

Ce dépôt contient le projet 2 d'étude pour le diplome data analyste
---

## Comment utiliser ce dépôt

### Cloner le projet
```bash
git clone https://github.com/<ton-utilisateur>/<nom-du-repo>.git
cd <nom-du-repo>
```

### Créer un environnement virtuel
```bash
uv venv
```

### Activer l’environnement virtuel
Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
Git Bash / macOS / Linux
```

```bash
source .venv/Scritps/activate
```

### Installer les dépendances
```bash
uv sync
```

### Lancer le projet
```bash
uv run python src/main.py
```

```bash
uv run python -m src.main.py
```