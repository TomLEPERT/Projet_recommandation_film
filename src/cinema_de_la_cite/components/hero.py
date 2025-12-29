import streamlit as st

def hero_section():
    st.markdown(
        """
        <style>
        .hero-container {
            background: linear-gradient(135deg, #111827, #1f2933);
            padding: 3rem 4rem;
            border-radius: 20px;
            color: white;
            margin-bottom: 2.5rem;
        }
        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            color: #d1d5db;
            margin-bottom: 1.5rem;
        }
        .hero-badges span {
            display: inline-block;
            background-color: #374151;
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            font-size: 0.9rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
        </style>

        <div class="hero-container">
            <div class="hero-title">🎬 Cinéma de la Cité</div>
            <div class="hero-subtitle">
                Découvrez, explorez et redécouvrez le cinéma français grâce à une recherche intelligente
                et un système de recommandations personnalisées.
            </div>
            <div class="hero-badges">
                <span>🇫🇷 Films français</span>
                <span>🔍 Recherche avancée</span>
                <span>🤖 Recommandation intelligente</span>
                <span>🎞️ Base TMDB</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )