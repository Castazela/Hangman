import mysql.connector as mysql

database = mysql.connect(
    host="localhost",
    user="root",
    password="root23805",
    database="hangman"
)


def adding_ligne_in_table(user_name, word_to_guess, trials_number, result):
    mycursor = database.cursor()
    add_line = "INSERT INTO game(user_id, word_to_guess, trials_number, losse_win) VALUES (%s, %s)"
    val = (user_name, word_to_guess, trials_number, result)
    return mycursor.execute(add_line, val)


def print_score_table():
    mycursor = database.cursor()
    mycursor.execute("SELECT * FROM game")
    myresult = mycursor.fetchall()
    return myresult
