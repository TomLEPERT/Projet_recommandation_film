## Objectif

Permettre à l’utilisateur·rice de créer un compte, s’authentifier et accéder à son espace personnel.
Cet espace lui permet de consulter et gérer :
- sa liste de favoris
- ses films aimés
- ses films non aimés
Ces données alimentent l’algorithme de recommandation afin d’affiner et personnaliser les propositions futures.

## Acteurs

- Utilisateur·rice
- Système (application Streamlit — backend de recommandations / base de données / CDN d’images)

## Préconditions

- L’application Streamlit est lancée et accessible via HTTPS.
- Le backend de gestion des utilisateurs est disponible (authentification, stockage sécurisé).
- L’utilisateur·rice doit disposer :
    - d’une pseudonyme valide pour créer son compte,
    - d’un mot de passe conforme aux règles de sécurité.
- L’utilisateur doit être connecté pour accéder aux listes personnelles (favoris, aimés, non aimés).

---

## Scénario principal
1. Création de compte
    - L’utilisateur·rice ouvre l’application Streamlit et navigue vers la page “Se connecter / Créer un compte” via le menu dédié.   
    - La page affiche deux options :
        “Se connecter”
        “Créer un compte”
    - L’utilisateur·rice clique sur “Créer un compte”.
        Le système affiche un formulaire Streamlit contenant :
            st.text_input("Pseudonyme")
            st.text_input("Mot de passe", type="password")
            st.text_input("Confirmer le mot de passe", type="password")
            Bouton st.button("Créer mon compte")
    - Lorsque l’utilisateur·rice appuie sur le bouton :
        Le système vérifie :
            que les deux mots de passe correspondent,
            que le pseudo n’est pas déjà enregistrée,
            que le mot de passe respecte les règles (longueur, complexité minimale).
            En cas d’erreur → un message clair s’affiche (st.error).
    - Si toutes les conditions sont valides :
        Le système crée un nouveau compte en base de données.
        Il initialise des listes vides : favoris[], aimés[], nonAimés[].
        Il affiche un message de succès : “Votre compte a été créé ! Vous pouvez maintenant vous connecter.”

2. Connexion
    - L’utilisateur·rice clique sur “Se connecter”.
        Streamlit affiche un formulaire :
            st.text_input("Adresse e-mail")
            st.text_input("Mot de passe", type="password")
            Bouton st.button("Connexion")
    - Le système vérifie les identifiants :
        si incorrects → st.error("Identifiants invalides")
        si corrects → création d’une session sécurisée via st.session_state["user_id"]
    - L’utilisateur·rice est redirigé·e vers son espace personnel.

3. Accès au compte
    - Dans la barre de navigation, l’utilisateur·rice clique sur “Mon compte”.
        Le système affiche une page contenant :
            Section “Mes favoris” (cartes de films)
            Section “Films aimés”
            Section “Films non aimés”
            Bouton Se déconnecter
    - Chaque film est affiché sous forme de carte Streamlit avec possibilité de :
        retirer des favoris,
        modifier “aimé / non aimé”,
        ouvrir la fiche du film.

4. Déconnexion
    - L’utilisateur·rice clique sur le bouton “Se déconnecter”.
    - Le système supprime la session (del st.session_state["user_id"]).
    - Un message confirme la déconnexion et l’utilisateur·rice est renvoyé·e vers l’accueil.

---
## Postconditions

- Le compte créé est stocké de manière sécurisée (mot de passe hashé).
- Les listes personnelles (favoris, aimés, non aimés) sont conservées et associées au compte utilisateur.
- L’utilisateur·rice connecté·e a accès à son espace personnel et ses actions (like, dislike, favoris) influencent l’algorithme.

---
## Critères d’acceptation (tests d’acceptation)

1. Création de compte réussie
Lorsque l’utilisateur·rice saisit un e-mail valide + mots de passe identiques, le système crée le compte et affiche un message de confirmation.
2. Connexion fonctionnelle
Avec des identifiants valides, l’utilisateur·rice est connecté·e et peut accéder à ses listes personnalisées.
3. Gestion des listes
Les actions “Ajouter aux favoris”, “J’aime”, “Je n’aime pas” sont visibles dans l’espace Mon compte et persistées après rafraîchissement.
4. Sécurité
Les mots de passe sont stockés hashés et aucune donnée sensible n’est affichée ni envoyée en clair.
5. Déconnexion
Cliquer sur “Se déconnecter” supprime la session utilisateur et désactive l’accès aux listes personnelles.