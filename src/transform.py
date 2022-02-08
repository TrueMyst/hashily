def reverse(char: str):
    return char[::-1]


def titlelize(char: str):
    words = ""

    for words in char.split():
        if len(words) > 0:
            words = words + " " + words.strip().lower().capitalize()
        else:
            words = words.capitalize()

    if not words:
        return char
    else:
        return words
