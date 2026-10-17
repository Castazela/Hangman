import mysql.connector as mysql
from tabulate import tabulate

database = mysql.connect(
    host="localhost",
    user="root",
    password="root23805",
    database="hangman"
)


def adding_ligne_in_table(user_name, word_to_guess, theme, trials_number, result):
    mycursor = database.cursor()
    add_line = "INSERT INTO score(user_id, word_to_guess, theme, trials_number, win_defeat) VALUES (%s, %s, %s, %s, %s)"
    val = (user_name, word_to_guess, theme, trials_number, result)
    mycursor.execute(add_line, val)
    database.commit()
    mycursor.close()


def get_score_table():
    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM score")
    myresult = mycursor.fetchall()
    mycursor.close()
    return tabulate(myresult, headers=["Partie n°","User", "Mot à deviner", "Thème", "Nombre d'essais", "Résultat"], tablefmt='pretty')
