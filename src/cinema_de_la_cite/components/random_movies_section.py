import streamlit as st
from components.stiker import call_stiker
from features.utils import select_movie

def random_movies_section():
    """
    Affiche les films aléatoires tant qu'aucune recherche n'est active
    """

    if "search_active" in st.session_state and st.session_state.search_active:
        return

    movies = st.session_state.get("random_movies", [])
    if not movies:
        return

    st.subheader("Suggestions aléatoires")

    cols = st.columns(5)

    for i, movie in enumerate(movies):
        with cols[i]:
            st.button(
                "Voir",
                key=f"random_{movie['imdb_id']}",
                on_click=select_movie,
                args=(movie,)
            )

            call_stiker(
                title=movie["title"],
                img=movie["poster"] or "",
                productor=movie["producers"],
                actors=movie["actors"],
                writters=", ".join(movie["writers"]),
                years=movie["year"],
                resumer=movie["summary"] or "",
                imbdbid=movie["imdb_id"]
            )
