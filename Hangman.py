#Import functions
from choosing_theme import choosing_theme
from file_to_words_list import read_file
from file_to_words_list import text_file_to_list
from file_to_words_list import normalize_word
#from random_word import random_word
#from word_progress import word_to_guess
#from word_progress import word_progression
#from error_manage import error_manager
#from secret import trophy

#Choosing theme and print random word to guess with underscores
theme_file = choosing_theme()
text = read_file(theme_file)
words_list = text_file_to_list(text)
new_words_list = [normalize_word(word) for word in words_list]
#random_word = random_word(new_words_list)
# word_to_guess = word_to_guess(random_word)
#test
#print(text)
#print(new_words_list)
#print(RandomWord)
# print("Le mot à trouver est :")
# print(' '.join(word_to_guess))

#Progression
#Choosing a letter and see if in the word or not
# progression = word_to_guess
# wrong_letter = ""
# error_counter = 0
# while True:
#     choosen_letter = input("Choisissez une lettre ! ")
#     progression = word_progression(choosen_letter,random_word, progression)
#     if progression == random_word:
#         print("C'est gagné !\nBRAVO !")
#         print(trophy)
#         break
#     if choosen_letter not in random_word:
#         error_counter, wrong_letter = error_manager(error_counter,choosen_letter, wrong_letter)
#         if error_counter == 10:
#             print("C'est perdu ! Le mot à deviner était :", random_word)
#             break
        
 

