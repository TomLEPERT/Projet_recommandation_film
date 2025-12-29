import streamlit as st
from features.recommender import (
    load_data,
    prepare_features,
    build_model,
    recommend_movies
)

@st.cache_resource
def load_recommender():
    df = load_data()
    X_scaled = prepare_features(df)
    model = build_model(X_scaled, n_neighbors=6)
    return df, model, X_scaled

