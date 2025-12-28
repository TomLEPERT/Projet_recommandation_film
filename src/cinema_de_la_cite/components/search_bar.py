import streamlit as st
import os
import pandas as pd
import ast
from math import ceil

from cinema_de_la_cite.features.clean_list_column import clean_list_column
from cinema_de_la_cite.features.build_response import build_response
from components.stiker import call_stiker
from features.utils import select_movie


def search_bar_widget(csv_path="data/tmdb_final_V3.csv", columns_per_row=4, page_size=8):

    # =========================
    # ÉTAT GLOBAL
    # =========================
    if "selected_movie" not in st.session_state:
        st.session_state.selected_movie = None
        
    if "search_results" not in st.session_state:
        st.session_state.search_results = None

    if "current_page" not in st.session_state:
        st.session_state.current_page = 1

    if "last_query" not in st.session_state:
        st.session_state.last_query = None

    # =========================
    # DATA
    # =========================
    @st.cache_data
    def load_data(csv_path):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV introuvable: {csv_path}")
        df = pd.read_csv(csv_path)

        data = {
            "Film": sorted(df["original_title"].dropna().unique().tolist()),
            "Genre": sorted(
                set(g for sub in df["genres_list"]
                    .dropna()
                    .apply(ast.literal_eval)
                    for g in sub)
            ),
            "Acteurs": sorted(
                set(a for sub in df["actor_list"]
                    .dropna()
                    .apply(clean_list_column)
                    for a in sub)
            ),
            "Producteurs": sorted(
                set(p for sub in df["production_companies_name_list"]
                    .dropna()
                    .apply(clean_list_column)
                    for p in sub)
            ),
            "Année": sorted(df["year"].dropna().astype(str).unique().tolist()),
            "Décennie": sorted(df["decade"].dropna().astype(str).unique().tolist()),
        }

        return df, data

    # =========================
    # UI RECHERCHE
    # =========================
    st.subheader("Rechercher un film")

    try:
        df, search_data = load_data(csv_path)
    except Exception as e:
        st.error(e)
        return None

    col1, col2, col3 = st.columns([2, 6, 1])

    with col1:
        search_type = st.selectbox("Type", list(search_data.keys()), label_visibility="collapsed")

    with col2:
        query = st.selectbox(
            "Recherche",
            options=search_data[search_type],
            index=None,
            placeholder="Commencez à taper…",
            label_visibility="collapsed"
        )

    with col3:
        submitted = st.button("Valider")

    # =========================
    # LOGIQUE RECHERCHE
    # =========================
    if submitted and query:

        st.session_state.search_active = True
        st.session_state.selected_movie = None

        # Recherche directe
        if search_type == "Film":
            movie_row = df[df["original_title"] == query].iloc[0]
            st.session_state.selected_movie = build_response(movie_row)

        # Recherche multiple
        else:
            if search_type == "Genre":
                results = df[df["genres_list"].apply(lambda x: query in ast.literal_eval(str(x)))]
            elif search_type == "Acteurs":
                results = df[df["actor_list"].str.contains(query, case=False, na=False)]
            elif search_type == "Producteurs":
                results = df[df["production_companies_name_list"].apply(lambda x: query in ast.literal_eval(str(x)))]
            elif search_type == "Année":
                results = df[df["year"].astype(str) == query]
            elif search_type == "Décennie":
                results = df[df["decade"].astype(str) == query]
            else:
                results = pd.DataFrame()

            if results.empty:
                st.info("Aucun film trouvé.")
                return None

            # Tri
            if "popularity" in results.columns:
                results = results.sort_values(["popularity", "original_title"], ascending=[False, True])
            else:
                results = results.sort_values("original_title")
            
            # Stockage des résultats
            st.session_state.search_results = results

    # Pagination
    results = st.session_state.search_results
    if results is None:
        return None

    total_pages = ceil(len(results) / page_size)

    page = st.number_input(
        "Page",
        min_value=1,
        max_value=total_pages,
        value=st.session_state.current_page,
        key="pagination_page"
    )

    st.session_state.current_page = page

    start = (page - 1) * page_size
    end = page * page_size
    page_results = results.iloc[start:end]

    movies = [build_response(row) for _, row in page_results.iterrows()]

    # Grille de stickers
    cols = st.columns(columns_per_row, gap="large")
    for idx, movie in enumerate(movies):
        with cols[idx % columns_per_row]:

            st.button(
                movie["title"],
                key=f"search_{movie['imdb_id']}",
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

    return None


