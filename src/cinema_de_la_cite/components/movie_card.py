import streamlit as st

from features.recommender_cache import load_recommender
from features.recommender import recommend_movies
from features.build_response import build_response
from components.stiker import call_stiker
from features.utils import select_movie

def movie_card(movie: dict):

    if movie is None:
        return

    df, model, X_scaled = load_recommender()

    # ========================
    # FILM PRINCIPAL
    # ========================
    col_img, col_info = st.columns([1, 2], gap="large")

    with col_img:
        if movie.get("poster"):
            st.image(movie["poster"], use_container_width=True)
        else:
            st.info("Affiche indisponible")

    with col_info:
        st.markdown(
            f"""
            <h1>{movie['title']}</h1>
            <p style="color:#9ca3af;">
                {movie['year']} • {", ".join(movie['genres'])}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Synopsis")
        st.write(movie["summary"] or "Résumé indisponible")

    st.divider()

    # ========================
    # INFOS
    # ========================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Acteurs")
        if movie.get("actors"):
            st.markdown(
                "".join(
                    f"<span class='actor-chip'>{a}</span>"
                    for a in movie["actors"][:12]
                ),
                unsafe_allow_html=True
            )

    with col2:
        st.markdown("### Production")
        st.write(", ".join(movie["producers"]) or "—")
        st.markdown("### Scénaristes")
        st.write(", ".join(movie["writers"]) or "—")

    # ========================
    # RECOMMANDATIONS
    # ========================
    st.divider()
    st.markdown("## Films similaires")

    reco_ids = recommend_movies(
        movie["imdb_id"],
        df,
        model,
        X_scaled,
        k=5
    )

    if reco_ids:
        cols = st.columns(5)
        for col, imdb_id in zip(cols, reco_ids):
            reco_row = df[df["imdb_id"] == imdb_id].iloc[0]
            reco_movie = build_response(reco_row)

            with col:
                st.button(
                    reco_movie["title"],
                    key=f"reco_{reco_movie['imdb_id']}",
                    on_click=select_movie,
                    args=(reco_movie,)
                )
                
                call_stiker(
                    title=reco_movie["title"],
                    img=reco_movie["poster"],
                    productor=reco_movie["producers"],
                    actors=reco_movie["actors"],
                    writters=", ".join(reco_movie["writers"]),
                    years=reco_movie["year"],
                    resumer=reco_movie["summary"],
                    imbdbid=reco_movie["imdb_id"]
                )
