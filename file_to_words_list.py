# Import
from unidecode import unidecode


def read_file(filename) -> list[str]:
    words_file = open(filename, 'rt', encoding='utf-8')
    text = words_file.readlines()
    words_file.close()
    return text


def text_file_to_list(text) -> list[str]:
    '''Creating a list of words from the file'''
    words_list = []
    for line in text:
        words_list += line.split()
    return words_list


def normalize_word(word) -> str:
    new_word = word.lower()
    new_word = unidecode(new_word)
    return new_word
