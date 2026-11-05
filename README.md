# Hangman game

## Fichiers actuellements utilisés dans le jeu
### Les fichiers permettant au joueur de jouer
- *get_random_word* effectue une requête SQL dans la table des thèmes de la base de données *hangam.sql* après que le joueur est choisi son thème
- *word_progress* permet la visualisation de la progression du joueur quand il joue. Les _ sont remplacés par les lettres si celles-ci sont justes.
- *main*

### Les fichiers ajoutant une "animation au jeu"
- *hangman* permet le dessin du pendu quand le joeur comment une erreur
- *draws* repertori 2 dessins affichés à la fin d'une partie en fonction de si le joeur gagne ou perd
- *score_table* effectue une requête SQL permettant l'afffichage du tableau des scores présent dans la base de donnée *hangam.sql*.


## Fichiers qui ne sont plus utilisés
-  *file_to_word_list* effectue la converstion des fichiers textes qui comptenaient les mots de chaque thème en liste de mots normalisés (sans majuscules ni accents).
-  *choosing_theme* permet au joueur de choisir un theme en lisant le titre des fichiers de theme.
-  *random_word* choisie un mot aléatoire parmis la liste créée par *file_to_word_list*.
