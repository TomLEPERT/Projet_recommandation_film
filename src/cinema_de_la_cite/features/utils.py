import streamlit as st

def select_movie(movie: dict):
    st.session_state.selected_movie = movie
    st.session_state.search_active = True
