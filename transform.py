def reverse(char: str):
    return char[::-1]

def titlelize(char: str):
    result = ""

    for words in char.split():
        if len(result) > 0:
            result = result + " " + words.strip().lower().capitalize()
        else:
            result = words.capitalize()

    if not result:
        return char
    else:
        return result

