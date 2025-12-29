import pandas as pd
import random
import streamlit as st
from cinema_de_la_cite.features.build_response import build_response

def load_random_movies(csv_path: str, n: int = 5):
    """
    Sélectionne n films aléatoires et les stocke dans le session_state
    """
    if "random_movies" in st.session_state:
        return

    df = pd.read_csv(csv_path)

    sampled = df.sample(n=n, random_state=random.randint(0, 10_000))
    movies = [build_response(row) for _, row in sampled.iterrows()]

    st.session_state.random_movies = movies
