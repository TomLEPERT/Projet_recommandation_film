import pandas as pd
from pathlib import Path

def save_dataframe_clean(df: pd.DataFrame, filename: str, project_root: Path, index: bool = False) -> None:
    """
    Sauvegarde un DataFrame dans le dossier 'data/clean' du projet, avec le nom de fichier fourni.

    Args:
        df (pd.DataFrame): Le DataFrame à sauvegarder.
        filename (str): Nom du fichier CSV (ex: "tmdb_clean.csv").
        project_root (Path): Chemin vers la racine du projet.
        index (bool): Inclure l'index dans le CSV ou non. Default = False.
    """
    # Chemin du dossier clean
    clean_folder = project_root / "data" / "clean"
    clean_folder.mkdir(parents=True, exist_ok=True)  # Crée le dossier s'il n'existe pas

    # Chemin complet du fichier
    output_path = clean_folder / filename

    # Sauvegarde
    df.to_csv(output_path, index=index)

r"""
UTILISATION

from cinema_de_la_cite.data.first_clean import clean_movies
from cinema_de_la_cite.data.save_dataframe_to_csv import save_dataframe_clean
from pathlib import Path

project_root = Path(r"F:\DataAnalystSimplon\Projet_recommandation_film")
df_clean = clean_movies(project_root / "data/row/tmdb_full.csv")

save_dataframe_clean(df_clean, "tmdb_clean.csv", project_root)

"""