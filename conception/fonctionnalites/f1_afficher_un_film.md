## Objectif

Permettre à l’utilisateur·rice de consulter la fiche détaillée d’un film proposé par le système de recommandation. L’affichage doit être clair, rapide et respecter les préférences de l’utilisateur (genres, localisation, valeurs éco-responsables).

## Acteurs

- Utilisateur·rice (connecté·e ou visiteur·se)
- Système (application Streamlit — backend de recommandations / base de données / CDN d’images)

## Préconditions

- L’application Streamlit est lancée et accessible via HTTPS.    
- Si l’utilisateur·rice souhaite sauvegarder un film dans ses favoris ou marquer un “J’aime”, il/elle doit être connecté·e.
- Les métadonnées du film (poster, titre, année, durée, pays, note IMDb, résumé, genres, acteurs, trailer URL) sont disponibles via l’API ou la base de données.
- Les préférences utilisateur (genres favoris, acteurs favoris, localisation) sont connues si l’utilisateur·rice est connecté·e.

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
        - Boutons d’action clairs :
            - **J’aime** / **Je n’aime pas** (`st.button`) — s’affiche différemment selon l’état.
            - **Ajouter aux favoris** (nécessite connexion).
            - **Recommandations similaires** (liste courte en bas).
    - Indications additionnelles : labels « Nouveauté », « Tendance locale », « Éco-friendly » si pertinents.
2. **Actions utilisateur**
    - Si l’utilisateur·rice clique **J’aime** :
        - Si connecté·e -> le système enregistre l’action et renvoie l’état mis à jour. L’interface met à jour immédiatement (optimistic UI).
        - Si non connecté·e -> le système affiche `st.warning("Connectez-vous pour enregistrer vos préférences")` et propose un bouton `Se connecter`.
    - Si l’utilisateur·rice clique **Passer** :
        - Le film est marqué comme non-pertinent (optionnel : `POST /user/{id}/skip`) et la liste de recommandations est recalculée/actualisée côté client.
3. **Retour / Navigation**
    - L’utilisateur·rice peut revenir à la liste (bouton `← Retour`) ou basculer vers d’autres onglets (ex. tendances locales, nouveautés).
    - Les changements visibles (like, favoris, skip) sont persistés et reflétés dans les recommandations suivantes.

---
## Postconditions

- Les indications d’intérêt (like/skip/favoris) sont correctement stockées en base avec timestamp et source (web/mobile).
- L’état visuel de la fiche et des cartes reflète la nouvelle donnée (ex. icône cœur remplie).
- Les recommandations se ré-adaptent (localement en mémoire ou via nouvelle requête).

---
## Critères d’acceptation (tests d’acceptation)

1. En tant qu’utilisateur connecté, je clique sur un film -> la fiche détaillée s’affiche avec poster, note, durée, pays et résumé complet.
2. En tant qu’utilisateur connecté, cliquer sur **J’aime** envoie une requête et l’icône change immédiatement ; après refresh, l’état est toujours activé.
3. En tant que visiteur, cliquer sur **Ajouter aux favoris** lance un message invitant à se connecter.
4. Les films marqués _skip_ n’apparaissent plus dans les 10 prochaines recommandations (si logique métier applicable).
5. Les posters se chargent via CDN et la page respecte un temps de chargement raisonnable (< 2s pour la vue principale sur connexion moyenne).
6. Les boutons sont accessibles au clavier et lisibles par lecteur d’écran (labels ARIA et textes alternatifs sur images).