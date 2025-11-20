from pathlib import Path
import pandas as pd
from cinema_de_la_cite.data.load_csv import load_csv

def clean_movies(csv_path: Path, language: str = "fr", min_vote: float = 6, exclude_genre: str = "TV Movie") -> pd.DataFrame:
    """
    Charge un CSV de films et retourne un DataFrame nettoyé selon certains critères.

    Args:
        csv_path (Path): Chemin vers le fichier CSV.
        language (str): Langue des films à garder. Default = "fr".
        min_vote (float): Note minimale des films. Default = 6.
        exclude_genre (str): Genre de films à exclure. Default = "TV Movie".

    Returns:
        pd.DataFrame: DataFrame filtré.
    """
    # Chargement du CSV
    df = load_csv(csv_path)
    
    # Filtrage par langue
    df = df[df["original_language"] == language]
    
    # Filtrage par note
    df = df[df["vote_average"] > min_vote]
    
    # Exclusion d'un genre
    df = df[df["genres"] != exclude_genre]
    
    return df

"""
UTILISATION

from cinema_de_la_cite.data.first_clean import clean_movies
csv_path = Path(r"F:\DataAnalystSimplon\Projet_recommandation_film\data\row\tmdb_full.csv")
df_clean = clean_movies(csv_path)
df_clean

"""


