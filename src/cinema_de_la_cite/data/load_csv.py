import pandas as pd
from pathlib import Path

def load_csv(path):
    """
    Charge un fichier CSV depuis un chemin donné.
    Paramètres
    ----------
    path : str ou Path
        Chemin complet du fichier CSV.

    Retour
    ------
    DataFrame pandas
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {path}")

    return pd.read_csv(path)

"""
UTILISATION

from pathlib import Path
from cinema_de_la_cite.data.load_csv import load_csv

# chemin vers ton CSV (à adapter)
csv_path = Path(r"F:\DataAnalystSimplon\Projet_recommandation_film\data\row\tmdb_full.csv")

df = load_csv(csv_path)
df

"""
