import random


def random_word(list_of_word: list[str]) -> str:
    random_word_to_guess = random.choice(list_of_word)
    return random_word_to_guess
