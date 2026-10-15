import mysql.connector as mysql

database = mysql.connect(
    host="localhost",
    user="root",
    password="root23805",
    database="hangman"
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
    10: "sport"}


def choosen_theme():
    print("Choisissez parmi ces thèmes:\n   1 : Fruits et légumes\n   2 : Instruments\n   3 : Métiers\n   4 : Animaux\n   5 : Villes Françaises\n   6 : Personnages de dessin animé\n   7 : Pays\n   8 : Couleurs\n   9 : Objets\n   10 : Sports")
    choice = int(input())
    theme = theme_list[choice]
    return theme


def get_random_word(theme):
    cursor = database.cursor()
    cursor.execute(
        "SELECT mot FROM words WHERE theme = %s ORDER BY RAND() LIMIT 1", (theme,))
    random_word = cursor.fetchone()
    return str(random_word[0])  # type: ignore
