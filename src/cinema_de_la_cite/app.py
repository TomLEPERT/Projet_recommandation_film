import streamlit as st
import os

# Définir les chemins relatifs à la racine
BASE_DIR = os.path.dirname("src/")

# Appel des components
from components.sidebar import call_sidebar

st.set_page_config(page_title="Cinéma de la cité", layout="wide")

call_sidebar()
