import streamlit as st
import os
import sys
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from cinema_de_la_cite.features.build_response import build_response

# Définir les chemins relatifs à la racine
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(
    BASE_DIR,
    "cinema_de_la_cite",
    "data",
    "tmdb_processed.csv"
)

# Appel des components
from components.sidebar import call_sidebar
from components.search_bar import search_bar_widget

st.set_page_config(page_title="Cinéma de la cité", layout="wide")

call_sidebar()

movie_row = search_bar_widget(csv_path=CSV_PATH)

if movie_row is not None:
    movie = build_response(movie_row)

    st.subheader(movie["title"])
    st.write(movie["summary"])

    if movie["poster"]:
        st.image(movie["poster"])

    st.json(movie)



