"""
Module de recommandation de films basé sur NearestNeighbors
Features :
- genres
- réalisateurs
- acteurs fréquents
- année de sortie
"""
import os
import sys
from pathlib import Path
import pandas as pd
import numpy as np

from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.neighbors import NearestNeighbors

from scipy.sparse import issparse

from features.transform_columns import transform_columns_to_list

# =========================
# Utils
# =========================
def to_dense(x) -> np.ndarray:
    """Convertit sparse -> dense sans casser le typage"""
    if issparse(x):
        return np.asarray(x.todense())
    return x

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "tmdb_final_V3.csv"
)

# =========================
# Chargement des données
# =========================
def load_data() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)

    columns_to_transform = [
        "genres_list",
        "actor_list",
        "director_names",
        "frequent_actors",
    ]

    df = transform_columns_to_list(df, columns_to_transform)

    return df

# =========================
# Préparation des features
# =========================
def prepare_features(df: pd.DataFrame) -> np.ndarray:
    mlb_genres = MultiLabelBinarizer()
    mlb_directors = MultiLabelBinarizer()
    mlb_actors = MultiLabelBinarizer()

    genres = to_dense(mlb_genres.fit_transform(df["genres_list"]))
    directors = to_dense(mlb_directors.fit_transform(df["director_names"]))
    actors = to_dense(mlb_actors.fit_transform(df["frequent_actors"]))
    years = df[["year"]].to_numpy()

    X = np.hstack((genres, directors, actors, years))

    scaler = StandardScaler()
    return scaler.fit_transform(X)

# =========================
# Construction du modèle
# =========================
def build_model(X: np.ndarray, n_neighbors: int = 6) -> NearestNeighbors:
    model = NearestNeighbors(
        n_neighbors=n_neighbors,
        metric="cosine",
        algorithm="auto"
    )
    model.fit(X)
    return model

# =========================
# Recommandation finale
# =========================
def recommend_movies(
    movie_id: str,
    df: pd.DataFrame,
    model: NearestNeighbors,
    X: np.ndarray,
    k: int = 5
) -> list[str]:

    if movie_id not in df["imdb_id"].values:
        raise ValueError(f"Film {movie_id} introuvable")

    movie_idx = df.index[df["imdb_id"] == movie_id][0]
    movie_vector = X[movie_idx].reshape(1, -1)

    distances, indices = model.kneighbors(movie_vector, n_neighbors=k + 1)

    recommendations = [
        df.iloc[i]["imdb_id"]
        for i in indices[0]
        if i != movie_idx
    ][:k]

    return recommendations