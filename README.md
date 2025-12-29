# Projet Python – Cinéma de la Cité

Application de recommandation de films – Streamlit
---

## Présentation du projet
Cinéma de la Cité est une application web développée avec Streamlit qui permet :

🔍 De rechercher des films selon plusieurs critères
🎞️ D’afficher des fiches films détaillées (affiche, synopsis, acteurs, production…)
⭐ De consulter la note moyenne du film
🤖 D’obtenir des recommandations de films similaires grâce à un algorithme de machine learning
🎲 De découvrir des films aléatoires au chargement de l’application
📊 D’explorer la base de données via des visualisations (page dédiée)

Le projet repose sur une base de données issue de TMDB / IMDb, enrichie et nettoyée, et vise à proposer des films français avec une  note de popularité supérieur ou égal à 6.

### Fonctionnalités principales

#### Recherche de films
Recherche possible par :
- Titre
- Genre
- Acteurs
- Producteurs
- Année
- Décennie

Résultats affichés sous forme de stickers interactifs avec pagination.

#### Stickers interactifs

Chaque film est affiché sous forme de carte visuelle :
- Affiche du film
- Hover avec infos clés (acteurs, production, année, note)
- Cliquable pour afficher la fiche détaillée

#### Fiche film (Movie Card)

Affichage détaillé :
- Affiche
- Titre
- Année
- Genres
- Note moyenne
- Synopsis (API externe)
- Acteurs
- Production & scénaristes

#### Recommandation de films

Un algorithme de recommandation basé sur Nearest Neighbors propose 5 films similaires à celui consulté.
Les critères utilisés :
- Genres
- Réalisateurs
- Acteurs fréquents
- Année de sortie

Résultat : recommandations cohérentes et pertinentes.

#### Films aléatoires

Au chargement de l’application :
- 5 films sélectionnés aléatoirement
- Disparaissent automatiquement lorsqu’une recherche est effectuée

#### Page Visualisation

Une page dédiée permet d’explorer la base de données via des graphiques :
- Acteurs les plus fréquents
- Répartition par genre
- Distribution des notes
- Notes moyennes par genre
- Durée médiane par décennie
- Top compagnies de production

### Architecture du projet
Projet_recommandation_film/
│
├── src/
│   └── cinema_de_la_cite/
│       ├── Accueil.py
│       ├── components/
│       │   ├── search_bar.py
│       │   ├── movie_card.py
│       │   ├── stiker.py
│       │   ├── random_movies_section.py
│       │   ├── sidebar.py
│       │   └── hero.py
│       │
│       ├── features/
│       │   ├── recommender.py
│       │   ├── recommender_cache.py
│       │   ├── build_response.py
│       │   ├── fetch_movie_details.py
│       │   ├── random_movies.py
│       │   ├── clean_list_column.py
│       │   └── utils.py
│       │
│       └── data/
│           └── tmdb_final_V3.csv
├── requirements.txt
└── README.md

### Technologies utilisées
- Python 3.10+
- Streamlit (interface web)
- Pandas / NumPy (traitement des données)
- Scikit-learn (recommandation)
- Matplotlib / Seaborn (visualisation)
- HTML / CSS (stickers & hover)
- API externe (TMDB / IMDb) pour posters & synopsis

### Algorithme de recommandation
Principe
- Encodage multi-label des genres, réalisateurs et acteurs
- Normalisation des features
- Calcul de similarité via cosine similarity
- Modèle : NearestNeighbors (scikit-learn)

Résultat
- Pour un film donné → 5 films les plus proches selon les caractéristiques.

### API externe (synopsis & affiches)

Les données visuelles et les synopsis sont récupérés via une API externe.
Pour fonctionner correctement :
- Lancer l’application
- Installer les dépendances
    pip install -r requirements.txt
- Lancer Streamlit
    streamlit run src/cinema_de_la_cite/app.py

### Améliorations possibles
- Authentification utilisateur
- Favoris & historique
- Filtres combinés
- Recommandation personnalisée
- Support multilingue

### Auteur

Projet réalisé dans le cadre d’un projet Data / Machine Learning
Formation Data Analyst – Simplon
- Tom Lepert
- Edouard Froment
- Maureen Moncheaux
- Jean-Baptiste LEDUC