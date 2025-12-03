## Objectif

Permettre à l’utilisateur·rice de consulter la fiche détaillée d’un film proposé par le système de recommandation. L’affichage doit être clair, rapide et respecter les préférences de l’utilisateur (genres, localisation, valeurs éco-responsables).

## Acteurs

- Utilisateur·rice
- Système (application Streamlit — backend de recommandations / base de données / CDN d’images)

## Préconditions

- L’application Streamlit est lancée et accessible via HTTPS.    
- Les métadonnées du film (poster, titre, année, durée, pays, note IMDb, résumé, genres, acteurs, trailer URL) sont disponibles via l’API ou la base de données.

---

## Scénario principal
1. **Affichage de la fiche détaillée**  
	 Déclenchement : l’utilisateur·rice clique sur la miniature ou le bouton **Détails**.
    - La page/section dédiée s’ouvre (ex. `st.expander` ou nouvelle vue) et affiche :
        - Poster grand format.
        - Titre, sous-titre (année • durée • pays).
        - Note IMDb + nombre d’avis (si disponible).
        - Résumé complet.
        - Genres, principaux acteurs (avec possibilité de cliquer pour voir autres films de l’acteur), réalisateur.
2. **Retour / Navigation**
    - L’utilisateur·rice peut revenir à la liste (bouton `← Retour`).

---
## Postconditions

---
## Critères d’acceptation (tests d’acceptation)

1. En tant qu’utilisateur connecté, je clique sur un film -> la fiche détaillée s’affiche avec poster, note, durée, pays et résumé complet.
2. Les posters se chargent via CDN et la page respecte un temps de chargement raisonnable (< 2s pour la vue principale sur connexion moyenne).
3. Les boutons sont accessibles au clavier et lisibles par lecteur d’écran (labels ARIA et textes alternatifs sur images).