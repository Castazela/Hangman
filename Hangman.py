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
# print(random_word)
word_to_guess_progression(random_word, [])

# Starting game
print("Proposez une lettre")
letter_list = []
error_counter = 0
letter_list.append(input())
word_progression = word_to_guess_progression(random_word, letter_list)

while (word_progression != random_word or error_counter != 10):
    print("Proposez une lettre")
    letter_list.append(input())
    word_progression = word_to_guess_progression(random_word, letter_list)
