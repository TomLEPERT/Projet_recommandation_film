#Objectif : 
Permettre à l'utilisateur de trouver rapidement le film idéal en fonction de ses préférences. (si compte client existant) ou en fonction de ses filtres. 

#Les fonctionnalités principales : 
- Une barre de recherche ou l'utilisateur pourra rechercher  par mot clés ou titre, acteur, film, genre, réalisateur ou décénie
- Un bouton permettant d'affiner le résultat de la recherche à côté de la barre principale. Les filtres = acteur / film / genre / réalisateur / décénie
- 

#Utilisation 
L'utilisateur entre sur l'application de recommandation de film, il choisi dans l'encadrement de filtrer par "film", il tape un mot clés en lien avec le titre et l'application lui propose les films ayant ce mot clés dans le titre. 
L'utilisateur devra cliquer sur le film choisi afin d'accéder à sa fiche et prendre connaissance de tous les détails liés au film choisi. 

#L'interface : 
Sur la page principal une barre de recherche se trouve en haut de la page ( en dessous du descriptif de l'application) , à sa gauche le bouton permettant d'effectuer un filtre et à la droite le bouton "valider" afin de lancer la recherche. 

#Scenario : 
Meihdi ouvre l'application de recommandation de film via streamlit, il souhaite trouver un film de comédie récent, il tape dans la barre de recherche comme mot clés "comédie" et il filtre sur la décénnie 2020. 
L'application lui proposera les comédies sorties depuis 2020 en fonction de ses précédentes recherches et films likés(si utilisateur connecté). 
Le résultat affiche les films avec : le titre, la note, l'affiche. Meihdi devra cliquer sur le film afin de pouvoir consulter sa fiche complète et prendre connaissance de la liste des acteurs, les prochaines séances au cinéma de la cité. 
