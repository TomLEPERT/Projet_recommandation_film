import streamlit as st
import os
import sys

SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from components.sidebar import call_sidebar
from components.search_bar import search_bar_widget
from components.hero import hero_section
from features.random_movies import load_random_movies
from components.random_movies_section import random_movies_section
from components.movie_card import movie_card

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(
    BASE_DIR,
    "cinema_de_la_cite",
    "data",
    "tmdb_processed.csv"
)

st.set_page_config(page_title="Cinéma de la cité", layout="wide")

# ========= CSS global =========
st.markdown(
    """
    <style>
    img {
        border-radius: 14px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.45);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    img:hover {
        transform: scale(1.03);
        box-shadow: 0 35px 70px rgba(0,0,0,0.6);
    }
    .actor-chip {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        margin: 0.25rem;
        background-color: #1f2933;
        color: #e5e7eb;
        border-radius: 999px;
        font-size: 0.9rem;
        border: 1px solid #374151;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ========= SESSION STATE =========
if "search_active" not in st.session_state:
    st.session_state.search_active = False

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# ========= UI =========
call_sidebar()
hero_section()

# ========= RANDOM MOVIES =========
load_random_movies(CSV_PATH)
random_movies_section()

# ========= SEARCH =========
movie = search_bar_widget(csv_path=CSV_PATH)

if movie:
    st.session_state.search_active = True

# ========= AFFICHAGE FILM =========
if st.session_state.selected_movie:
    st.divider()
    movie_card(st.session_state.selected_movie)
