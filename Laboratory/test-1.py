def Caesar(char: str, shift: int = 3):
    caesar = ""

    for i in range(len(char)):
        if char[i].isupper():
            caesar += chr((ord(char[i]) + shift - 65) % 26 + 65)

        elif char[i].islower():
            caesar += chr((ord(char[i]) + shift - 97) % 26 + 97)
        else:
            caesar += char[i]

    return caesar


class A1Z26():
    def encode(char: str):
        A1Z26 = []

        for i in char:
            if i.isalpha():
                A1Z26.append(str(ord(i.lower()) - 96))
            else:
                A1Z26.append(i)

        return " ".join(A1Z26)


print(A1Z26.decode("8 5 12 12 15   23 15 18 12 4"))