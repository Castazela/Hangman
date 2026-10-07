# Import functions
from choosing_theme import choosing_theme
from file_to_words_list import read_file
from file_to_words_list import text_file_to_list
from file_to_words_list import normalize_word
from random_word import random_word
from word_progress import word_to_guess_progression
# from error_manage import error_manager
# from secret import trophy

# Choosing theme and print random word to guess with underscores
theme_file = choosing_theme()
text = read_file(theme_file)
words_list = text_file_to_list(text)
new_words_list = [normalize_word(word) for word in words_list]
random_word = random_word(new_words_list)
print("Le mot à deviner est : ")
print("ceci est random_word", random_word)
word_to_guess_progression(random_word, [])

# Starting game
print("Proposez une lettre")
letter_list = []
error_counter = 0
letter_list.append(input())
word_progression = (word_to_guess_progression(random_word, letter_list))

# test
print(repr(word_progression), repr(random_word), error_counter)

while not (word_progression == random_word or error_counter >= 10):
    print("Proposez une lettre")
    proposed_letter = input()
    letter_list.append(proposed_letter)
    if proposed_letter in random_word:
        word_progression = (word_to_guess_progression(
            random_word, letter_list)).replace(" ", "")
    else:
        error_counter += 1
    # test
    print(repr(word_progression), repr(random_word), error_counter)
    # print("Ceci est word_gest_progression", word_progression)
