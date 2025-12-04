## Objectif

Permettre à l’utilisateur·rice de consulter une liste de 4 films dès la page d'accueil. 
Note : cette fonctionnalité est différente de la liste de recommndation, même si la forme sera la même (format, infos visibles lors du survol, etc.).
L’affichage doit être clair et rapide. Cette liste de 4 films sera l'affichage par défaut lors de la connexion sur lapp. Elle se placera sous la barre de système de recherche. Cette liste de 4 films sera composée de 4 films aléatoires.
Les 4 affiches seront présentées centrés sur la page et répartis équitablement (en 4 colonnes).

## Acteurs

- Utilisateur·rice (connecté·e ou visiteur·se)
- Système (application Streamlit — backend de recommandations / base de données / CDN d’images)

## Préconditions

- L’application Streamlit est lancée et accessible via HTTPS.    
- Cette liste ne s'affiche que sur la page d'accueil, car c'est la liste à défaut.
- si la liste de recommandation a été lancée, elle prend le dessus sur la fonctionnalité liste de films.

---

## Scénario principal
1. **Affichage de la liste de films**  
	- Déclenchement : elle s'affiche par défaut lors de la connexion à l'app
    - elle est composée de 4 films (avec l'affiche et le nom du film)
2. **Actions utilisateur**
    - le survol de l'affiche permettra d'afficher d'autres informations (au même titre que la fonctionnalité liste de recommandation)
    - un clic sur lun des éléments (affiche ou titre) déclenchera l'ouverture du film choisi sur la partie centrale
    - le clic chargera aussi 4 nouveaux films basés sur la fonctionnalité recommndation de films

---
## Critères d’acceptation (tests d’acceptation)

1. En tant qu’utilisateur, je vois lors de ma 1ère connexion 4 films aléatoires.
2. Les affiches et les titres s'affichent correctement