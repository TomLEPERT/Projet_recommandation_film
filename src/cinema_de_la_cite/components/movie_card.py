import streamlit as st

def movie_card(movie: dict):
    
    if movie is None:
        return

    col_img, col_info = st.columns([1, 2], gap="large")

    with col_img:
        if movie.get("poster"):
            st.image(movie["poster"], width="stretch")
        else:
            st.info("Affiche indisponible")

    with col_info:
        st.markdown(
            f"""
            <h1 style="margin-bottom: 0.2rem;">{movie['title']}</h1>
            <p style="color: #9ca3af; font-size: 1.1rem;">
                {movie['year']} • {", ".join(movie['genres'])}
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("### Synopsis")
        st.write(movie["summary"] or "Résumé indisponible")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Acteurs")
        actors = movie.get("actors", [])

        if actors:
            chips_html = "".join(
                f"<span class='actor-chip'>{actor}</span>"
                for actor in actors[:12]
            )
            st.markdown(chips_html, unsafe_allow_html=True)
        else:
            st.write("Non renseigné")

    with col2:
        st.markdown("### Production")
        st.write(", ".join(movie["producers"]) or "Non renseigné")
        st.markdown("### Scénariste")
        st.write(", ".join(movie["writers"]) or "Non renseigné")