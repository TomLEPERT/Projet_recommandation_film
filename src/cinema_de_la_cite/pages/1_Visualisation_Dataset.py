import ast
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualisation BDD",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(
    BASE_DIR,
    "data",
    "tmdb_final_V3.csv"
)

df_final = pd.read_csv(CSV_PATH)

st.title("Présentation du Dataset - Visualisation des graphiques")  
st.header("Nous avons ici la possibilité de voir les graphiques réalisés lors de l'étude des données.")

graphique = st.selectbox("Veuillez sélectionner un graphique :",
    ["Acteurs les plus représentés", 
     "Répartition des films par genre", 
     "Répartition des notes par tranches", 
     "Distribution des notes des films", 
     "Note moyenne par genre", 
     "Durée médiane des films par décennie", 
     "top 5 des compagnies de production"]
)

# -------------------------------
# Acteurs les plus représentés
# -------------------------------
if graphique == "Acteurs les plus représentés":
    st.write("Graphique des meilleurs acteurs.")
    top_actors = (df_final["frequent_actors"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .str.replace("'", " ")
        .str.replace("[", " ")
    )
    top_actors = top_actors[~top_actors.str.contains("Unknown", na=False)]
    top_actors = top_actors.value_counts().head(15).sort_values(ascending=True)

    plt.figure(figsize=(8,6))
    plt.barh(list(top_actors.index), list(top_actors.values),
            color=["#7FA9F7", "#FFA3A6", "#FFE08A", "#70D8B0"],
            edgecolor="black")
    for idx, value in enumerate(top_actors.values):
        plt.text(float(value)+0.5, idx, str(int(value)), va='center', fontsize=10)

    plt.title("Acteurs les plus fréquents")
    plt.xlabel("Nombre de films")
    plt.ylabel("Acteurs")
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Répartition des films par genre
# -------------------------------
if graphique == "Répartition des films par genre":
    st.write("Graphique de la répartition des films par genre.")
    df_final['genres_list'] = df_final['genres_list'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    df_exploded = df_final.explode('genres_list')
    df_exploded['genres_list'] = df_exploded['genres_list'].str.strip()
    genre_counts = df_exploded['genres_list'].value_counts().reset_index()
    genre_counts.columns = ['Genre', 'Nombre']
    color=["#7FA9F7", "#FFA3A6", "#FFE08A", "#70D8B0"]

    plt.figure(figsize=(10,6))
    barplot = sns.barplot(x='Genre', y='Nombre', data=genre_counts, palette=color)
    y_values = pd.to_numeric(genre_counts['Nombre'], errors='coerce').fillna(0).astype(float)

    for idx, y in enumerate(y_values):
        barplot.text(idx, y + 0.5, str(int(y)), ha='center', color='black')

    plt.xticks(rotation=45)
    plt.title('Répartition des films par genre', fontsize=20, fontweight='bold')
    plt.ylabel('Nombre de films', fontweight='bold')
    plt.xlabel('Genre', fontweight='bold')
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Répartition des notes par tranches
# -------------------------------
if graphique == "Répartition des notes par tranches":
    st.write("Graphique de la répartition des notes par tranches.")
    bins = [6,7,8,9,10.01]
    labels = ['6-7','7-8','8-9','9-10']
    df_final['slice_notes'] = pd.cut(df_final['vote_average'], bins=bins, labels=labels, right=False)
    couleurs = ['#7FA9F7', '#FFA3A6', '#FFE08A', '#70D8B0']
    pourcentage = round(df_final['slice_notes'].value_counts(normalize=True)*100,1)
    plt.figure(figsize=(12,10))
    plt.pie(pourcentage, autopct='%1.0f%%', startangle=90, colors=couleurs, textprops={'fontsize':18})
    plt.title("Répartition des notes par tranches", fontsize=20, fontweight='bold')
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Distribution des notes des films
# -------------------------------
if graphique == "Distribution des notes des films":
    st.write("Graphique de la distribution des notes des films.")
    plt.figure(figsize=(6,6))
    sns.boxplot(y=df_final['vote_average'], color='#3D6BEB')
    plt.title("Distribution des notes des films", fontsize=18, fontweight='bold')
    plt.ylabel("Vote moyen", fontsize=14)
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Note moyenne par genre
# -------------------------------
if graphique == "Note moyenne par genre":
    st.write("Graphique de la note moyenne par genre.")
    df_final['genres_list'] = df_final['genres_list'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    genres_explode = df_final.explode("genres_list")
    mean_by_genre = genres_explode.groupby("genres_list")["vote_average"].mean().sort_values(ascending=True)

    plt.figure(figsize=(12,8))
    plt.barh(list(mean_by_genre.index), list(mean_by_genre.values),
            color=['#7FA9F7', '#FFA3A6', '#FFE08A', '#70D8B0'], edgecolor='black')
    for idx, value in enumerate(mean_by_genre.values):
        plt.text(float(value)+0.05, idx, str(round(float(value),2)), va='center', fontsize=10)

    plt.title("Note moyenne par genre (Films FR)", fontsize=18, fontweight='bold')
    plt.xlabel("Note moyenne")
    plt.ylabel("Genre")
    plt.grid(axis="x", linestyle="--", alpha=0.4)
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Durée médiane des films par décennie
# -------------------------------
if graphique == "Durée médiane des films par décennie":
    st.write("Graphique de la durée médiane des films par décennie.")   
    df_final["decade"] = (df_final["year"] // 10) * 10
    median_runtime = df_final.groupby("decade")["runtime"].median().sort_index()

    plt.figure(figsize=(8,5))
    plt.plot(list(median_runtime.index), list(median_runtime.values),
            marker='o', color='#3A86FF', linewidth=2)
    for x, y in zip(list(median_runtime.index), list(median_runtime.values)):
        plt.text(float(x), float(y)+1, str(int(y)), ha='center', fontsize=10)

    plt.title("Durée médiane des films par décennie", fontsize=18, fontweight='bold')
    plt.xlabel("Décennie")
    plt.ylabel("Durée médiane (minutes)")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.close()

# -------------------------------
# Top 5 des compagnies de production
# -------------------------------
if graphique == "top 5 des compagnies de production":
    st.write("Graphique du top 5 des compagnies de production.")
    seuil = 6
    df_filtrer = df_final[(df_final['original_language']=='fr') & (df_final['vote_average']>=seuil)]
    df_subset = df_filtrer.iloc[1:]
    top_companies = df_subset['production_companies_name_list'].value_counts()
    top_5_from_second = top_companies.iloc[1:6]

    couleurs = ['#7FA9F7', '#FFA3A6', '#FFE08A', '#70D8B0','#3D6BEB']
    plt.figure(figsize=(8,8))
    plt.pie(list(top_5_from_second), labels=list(top_5_from_second.index), autopct='%1.1f%%',
            startangle=140, colors=couleurs)
    plt.title("Top 5 des compagnies de production", fontweight='bold', fontsize=14)
    st.pyplot(plt.gcf())
    plt.close()
