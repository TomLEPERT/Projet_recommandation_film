## Objectif
permettre à l'utilisateur de se connecter à son compte client afin de pouvoir consulter les recommandations de film et trouver la séance du moment dans le cinéma de la cité. 

## Acteurs : 
- Utilisateur·rice
- Système (application Streamlit — backend de recommandations / base de données / CDN d’images)

## Préconditions

- L’application Streamlit est lancée et accessible via HTTPS.    
- Les métadonnées du film (poster, titre, année, durée, pays, note IMDb, résumé, genres, acteurs, trailer URL) sont disponibles via l’API ou la base de données.
- Les données des séances du moment

## Scénario principal
1. Connexion 
- L'utilisateur ouvre l'application Streamlit et navigue vers la page et clique sur "se connecter" via le menu. 
- La page affiche " se connecter"
- L'utilisateur clique sur "se connecter" et rentre son pseudo et son mot de passe puis clique sur le bouton "connexion"
Le système vérifie si le pseudo et mdp sont reliés a un compte d'utilisateur enregistré dans la base de donnée. 

2. Navigation : 
- L'utilisateur accède a la page d'accueil, il clique sur l'onglet "séance du moment" 
- Une page s'affiche avec les séances du moment dans le cinéma "cinéma de la cité à Angoulême".
- L'utilisateur pourra choisir le jour de la séance choisi
Le système lui affiche : 
        - Poster grand format.
        - Titre
- L'utilisateur choisi le film qu'il souhaite voir en cliquant sur son affiche ou le titre
 Le système affiche : 
      - Poster grand format.
      - Titre, sous-titre (année • durée • pays).
      - Note IMDb + nombre d’avis (si disponible).
      - Résumé complet.
      - Genres, principaux acteurs (avec possibilité de cliquer pour voir autres films de l’acteur), réalisateur.
      -  Les heures des séances sur la date sélectionné.

## Critères d’acceptation (tests d’acceptation)