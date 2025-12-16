"""
Module de recommandation de films basé sur NearestNeighbors
avec les colonnes : genres, directeurs, acteurs fréquents, année.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.neighbors import NearestNeighbors

# Import de la fonction utilitaire (même dossier)
from transform_columns import transform_columns_to_list

# -------------------------
# 1. Chargement du DataFrame
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent  # remonte jusqu'à Projet_recommandation_film
DATA_FILE = BASE_DIR / "data" / "clean" / "tmdb_final_V3.csv"

def load_data():
    """Charge le DataFrame et transforme les colonnes en listes"""
    df = pd.read_csv(DATA_FILE)

    # Colonnes à transformer
    columns_to_transform = ["genres_list", "actor_list", "director_names", "frequent_actors"]
    df = transform_columns_to_list(df, columns_to_transform)

    return df

# -------------------------
# 2. Préparation des features
# -------------------------
def prepare_features(df):
    mlb_genres = MultiLabelBinarizer()
    mlb_directors = MultiLabelBinarizer()
    mlb_actors = MultiLabelBinarizer()

    genres_encode = mlb_genres.fit_transform(df["genres_list"])
    directors_encode = mlb_directors.fit_transform(df["director_names"])
    frequent_actors_encode = mlb_actors.fit_transform(df["frequent_actors"])
    year_encode = df[["year"]].values

    X = np.hstack([genres_encode, directors_encode, frequent_actors_encode, year_encode])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled

# -------------------------
# 3. Construction du modèle
# -------------------------
def build_model(X_scaled, n_neighbors=5):
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='auto', metric='cosine')
    model.fit(X_scaled)
    return model

# -------------------------
# 4. Fonction principale de recommandation
# -------------------------
def recommend_movies(movie_id, df=None, model=None, X_scaled=None, k=4):
    if df is None or model is None or X_scaled is None:
        df = load_data()
        X_scaled = prepare_features(df)
        model = build_model(X_scaled, n_neighbors=k+1)

    if movie_id not in df["imdb_id"].values:
        raise ValueError(f"movie_id '{movie_id}' introuvable dans le dataset.")

    movie_idx = df.index[df["imdb_id"] == movie_id][0]
    movie_vector = X_scaled[movie_idx].reshape(1, -1)
    distances, indices = model.kneighbors(movie_vector, n_neighbors=k+1)
    recommended_indices = [i for i in indices[0] if i != movie_idx][:k]
    recommended_ids = df.iloc[recommended_indices]["imdb_id"].tolist()
    return recommended_ids

# -------------------------
# Test si exécution directe
# -------------------------
if __name__ == "__main__":
    df_movies = load_data()
    X_scaled = prepare_features(df_movies)
    nn_model = build_model(X_scaled, n_neighbors=5)  # 4 voisins + le film lui-même

    test_movie_id = "tt0100263"  # Nikita
    recommandations = recommend_movies(test_movie_id, df_movies, nn_model, X_scaled, k=4)
    print(f"Recommandations pour '{test_movie_id}': {recommandations}")
    

# -----------------------------------------------------------------------------
# NOTE D'UTILISATION DANS UN AUTRE SCRIPT
# -----------------------------------------------------------------------------
# Pour utiliser la fonction recommend_movies() dans un autre script :
#
# 1. Importer les fonctions depuis ce module :
#    from src.cinema_de_la_cite.features.recommender import (
#        load_data,
#        prepare_features,
#        build_model,
#        recommend_movies
#    )
#
# 2. Charger les données et préparer le modèle (une seule fois pour plusieurs recommandations) :
#    df = load_data()
#    X_scaled = prepare_features(df)
#    model = build_model(X_scaled, n_neighbors=5)  # k+1 pour inclure le film lui-même
#
# 3. Appeler recommend_movies() avec le film désiré et le modèle préparé :
#    movie_id = "tt0100263"  # exemple : Nikita
#    recommandations = recommend_movies(movie_id, df, model, X_scaled, k=4)
#    print(recommandations)
#
# Notes :
# - df : DataFrame chargé avec load_data()
# - model : modèle NearestNeighbors entraîné
# - X_scaled : matrice des features standardisée
# - k : nombre de films recommandés (par défaut 4)
# -----------------------------------------------------------------------------