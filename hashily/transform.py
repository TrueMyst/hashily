def reverse(char: str):
    return char[::-1]


def titlelize(char: str):
    return " ".join(i.strip().lower().capitalize() for i in char.split())
