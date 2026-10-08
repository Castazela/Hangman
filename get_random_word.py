'''theme_list :
    1: "fruit_legume",
    2: "instrument",
    3: "métier",
    4: "animaux",
    5: "ville_française",
    6: "personnage",
    7: "pays",
    8: "couleur",
    9: "objet",
    10: "sport"'''

import _mysql_connector as mysql

database = mysql.connect(
    host="localhost",
    user="user",
    passwd="password",
    database="hangman"
)


def choosing_theme():
    print("Choisissez parmis ces thèmes:\n   1 : Fruits et légumes\n   2 : Instruments)\n   3 : Métiers\n   4 : Animaux\n   5 : Villes Françaises\n   6 : Pays\n   7 : Couleurs\n   8 : Objets\n   9 : Sports")
    choice = int(input())
    match choice:
    case 1:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'fruit_legume'")
    case 2:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 3:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 4:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 5:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 6:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 7:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 8:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case 9:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
    case _:
        cursor = database.cursor()
        cursor.execute("SELECT RAND() FROM mots WHERE theme = 'instrument'")
