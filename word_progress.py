def word_to_guess(word: str, proposed_letter: list[str]) -> str:
    word_to_return: list[str] = []
    for letter in word:
        if letter in proposed_letter:
            word_to_return.append(letter)
        else:
            word_to_return.append("_ ")
    print(" ".join(word_to_return))
    return " ".join(word_to_return)
