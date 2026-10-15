# Import functions
# from choosing_theme import choosing_theme
# from file_to_words_list import read_file
# from file_to_words_list import text_file_to_list
from file_to_words_list import normalize_word
# from random_word import random_word
from get_random_word import get_random_word
from get_random_word import choosen_theme
from word_progress import word_to_guess_progression
from hangman import hangman
from draws import trophy
from draws import loser
from score_table import adding_ligne_in_table
from score_table import get_score_table

# Choosing theme and print random word to guess with underscores
# theme_file = choosing_theme()
# text = read_file(theme_file)
# words_list = text_file_to_list(text)
# new_words_list = [normalize_word(word) for word in words_list]
# random_word = random_word(new_words_list)
# test
# print("random word :", random_word)

# Game menu
print("Que souhaitez vous faire ? \n1. Jouer au jeu\n2. Voir le tableau des scores")
menu = int(input())

if menu == 1:
    # Starting gramme
    print("Entrez un nom d'utilisateur")
    user = input()
    theme = choosen_theme()
    random_word = normalize_word(get_random_word(theme))
    word_progression = word_to_guess_progression(
        random_word, []).replace(" ", "")
    print("Le mot à deviner est : ")
    print(word_progression)
    letter_list = []
    wrong_letters = []
    error_counter = 0
    try_number = 0
    # test
    # print(repr(word_progression), repr(random_word), error_counter)
    while not (word_progression == random_word or error_counter == 10):
        print("Proposez une lettre")
        proposed_letter = input().lower()
        try_number += 1
        if len(proposed_letter) != 1 or not proposed_letter.isalpha():
            print("Entrée erronée")
        else:
            if proposed_letter not in letter_list:
                letter_list.append(proposed_letter)
                if proposed_letter in random_word:
                    word_progression = (word_to_guess_progression(
                        random_word, letter_list)).replace(" ", "")
                else:
                    error_counter += 1
                    wrong_letters.append(proposed_letter)
                    # print("Nombre d'erreur :", error_counter)
                    print("Cette lettre n'est pas dans le mot ! \n Les lettres incorrectes déjà proposées sont :", " ".join(
                        wrong_letters))
                    print(hangman[error_counter])
                print(word_progression)
                # test
                # print(repr(word_progression), repr(random_word), error_counter)
            else:  # proposed lettre in letter list
                print("Cette lettre a déjà été proposée")

    if word_progression == random_word:
        result = "Win"
        adding_ligne_in_table(user, random_word, theme, try_number, result)
        print("C'est gagné !\nVous avez trouvé en", try_number, "essais.")
        print(trophy)

    else:
        if error_counter == 10:
            result = "Loose"
            adding_ligne_in_table(user, random_word, theme, try_number, result)
            print("C'est perdu ! \n Le mot à deviné était :", random_word)
            print(loser)

else:  # tableau des scores
    print(get_score_table())
