from utils.exceptions import CustomValueError


class ROT13():

    @staticmethod
    def encode(char: str):
        return char.translate(bytes.maketrans(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', b'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

    @staticmethod
    def decode(char: str):
        return char.translate(bytes.maketrans(b'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm', b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))


class AtBash():
    @staticmethod
    def encode(char):
        AtBash = ""

        for letters in char:
            if letters.isupper():
                Code = ord('Z') + ord('A')
                AtBash += chr(Code - ord(letters))

            elif letters.islower():
                Code = ord('z') + ord('a')
                AtBash += chr(Code - ord(letters))

            else:
                AtBash += letters

        return AtBash

    @staticmethod
    def decode(char: str):
        AtBash = ""

        for letters in char:
            if letters.isupper():
                Code = ord('Z') + ord('A')
                AtBash += chr(Code - ord(letters))

            elif letters.islower():
                Code = ord('z') + ord('a')
                AtBash += chr(Code - ord(letters))

            else:
                AtBash += letters

        return AtBash


class Bacon():

    def encode(char: str):
        BaconDict = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
                     'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
                     'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
                     'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
                     'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
                     'Z': 'bbaab'}

        return char.upper().translate(str.maketrans(BaconDict))

    def decode(char: str):
        BaconDict = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
                     'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
                     'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
                     'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
                     'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
                     'Z': 'bbaab'}

        BaconText = ''
        i = 0

        while True:
            if(i < len(char)-4):
                sets = char[i:i + 5]
                if sets[0] != ' ':
                    BaconText += list(BaconDict.keys()
                                      )[list(BaconDict.values()).index(sets)].lower()
                    i += 5

                else:
                    BaconText += ' '
                    i += 1
            else:
                break

        return BaconText


class A1Z26():
    def encode(char: str):
        A1Z26 = []

        for i in char:
            if i.isalpha():
                A1Z26.append(str(ord(i.lower()) - 96))

            else:
                A1Z26.append(i)

        for i in range(len(A1Z26)):
            if A1Z26[i] == " ":
                A1Z26[i] = ""

        return " ".join(A1Z26)

    def decode(char: str):
        A1Z26 = []

        for i in char.split(" "):
            if i != "":
                A1Z26.append(chr(int(i) + 96))

            else:
                A1Z26.append(" ")

        return "".join(A1Z26)


class Caesar():

    def encode(char: str, shift: int = 3):
        caesar = ""

        for i in range(len(char)):
            if char[i].isupper():
                caesar += chr((ord(char[i]) + shift - 65) % 26 + 65)

            elif char[i].islower():
                caesar += chr((ord(char[i]) + shift - 97) % 26 + 97)
            else:
                caesar += char[i]

        return caesar

    def decode(char: str, shift: int = 3):
        caesar = ""

        for i in range(len(char)):
            if char[i].isupper():
                caesar += chr((ord(char[i]) - shift - 65) % 26 + 65)

            elif char[i].islower():
                caesar += chr((ord(char[i]) - shift - 97) % 26 + 97)
            else:
                caesar += char[i]

        return caesar
