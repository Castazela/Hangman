'''All theme from dataset :
        - fruits et legumes
        - instruments
        - métiers
        - animaux
        - villes-fr
        - pays
        - couleurs
        - objets
        - sports'''

import _mysql_connector as mysql

database = mysql.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="hangman.sql"
)

theme_list = {
    1: "fruit_legume",
    2: "instrument",
    3: "métier",
    4: "animaux",
    5: "ville_française",
    6: "personnage",
    7: "pays",
    8: "couleur",
    9: "objet",
    10: "sport"
}
