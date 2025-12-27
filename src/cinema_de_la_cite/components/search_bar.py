import streamlit as st
import os
import pandas as pd
import ast

from cinema_de_la_cite.features.clean_list_column import clean_list_column

def search_bar_widget(csv_path = "data/tmdb_processed.csv"):
    @st.cache_data
    def load_data(csv_path):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV introuvable: {csv_path}")
        df = pd.read_csv(csv_path)

        data = {
            "Film": sorted(df['original_title'].dropna().unique().tolist()),
            "Genre": sorted(
                set(g for sub in df['genres_list']
                    .dropna()
                    .apply(ast.literal_eval) 
                    for g in sub
                )
            ),
            "Acteurs": sorted(
                set(
                    a 
                    for sub in df['actor_list']
                    .dropna()
                    .apply(clean_list_column)
                    for a in sub
                )
            ),
            "Producteurs": sorted(
                set(
                    p 
                    for sub in df['production_companies_name_list']
                    .dropna()
                    .apply(clean_list_column) 
                    for p in sub
                )
            ),
            "Année": sorted(df['year'].dropna().astype(str).unique().tolist()),
            "Décennie": sorted(df['decade'].dropna().astype(str).unique().tolist()),
        }

        return df, data

    st.write("### Recherchez un film")
    
    try:
        df, search_data = load_data(csv_path)
    except Exception as e:
        st.error(e)
        return None

    col1, col2, col3 = st.columns([2, 6, 1])

    with col1:
        search_type = st.selectbox(
            "Type",
            list(search_data.keys()),
            label_visibility="collapsed"
        )

    with col2:
        query = st.selectbox(
            "Recherche",
            options=search_data[search_type],
            index=None,
            placeholder="Commencez à taper...",
            label_visibility="collapsed"
        )

    with col3:
        submitted = st.button("Valider")

    if submitted and query:
        if search_type == "Film":
            movie_row = df[df['original_title'] == query].iloc[0]

        elif search_type == "Genre":
            results = df[df['genres_list'].apply(
                lambda x: query in ast.literal_eval(str(x))
            )]

        elif search_type == "Acteurs":
            results = df[df['actor_list'].str.contains(query, case=False, na=False)]

        elif search_type == "Producteurs":
            results = df[df['production_companies_name_list'].apply(
                lambda x: query in ast.literal_eval(str(x))
            )]

        elif search_type == "Année":
            results = df[df['year'].astype(str) == query]

        elif search_type == "Décennie":
            results = df[df['decade'].astype(str) == query]

        else:
            results = pd.DataFrame()

        st.write(f"### Résultats pour **{query}**")
        st.dataframe(movie_row)
        
        return movie_row
    
    st.write(search_data)
    return None