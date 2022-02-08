import urllib.parse

class Binary:
    @staticmethod
    def encode(char: str):
        return " ".join(format(ord(i), '08b') for i in char.strip())

    @staticmethod
    def decode(char: int):
            return "".join(chr(int(i, 2)) for i in char.strip().split(" "))


class Hexadecimal:
    @staticmethod
    def encode(char: str):
        return " ".join(format(ord(i), 'x') for i in char)

    @staticmethod
    def decode(char: str):
        return "".join(chr(int(i, 16)) for i in char.strip().split(" "))


class Octal:
    @staticmethod
    def encode(char: str):
        return " ".join(format(ord(i), 'o') for i in char)

    @staticmethod
    def decode(char: str):
        return "".join(chr(int(i, 8)) for i in char.strip().split(" "))


class Integer:
    @staticmethod
    def encode(char: str):
        return " ".join([str(ord(i)) for i in char])

    @staticmethod
    def decode(char):
        return "".join([chr(int(i)) for i in str(char).split(" ")])


class UrlEncoding:
    @staticmethod
    def encode(char: str):
        return urllib.parse.quote(char)

    @staticmethod
    def decode(char: str):
        return urllib.parse.unquote(char)


class UnicodePoint:
    @staticmethod
    def encode(char):
        return " ".join([str(hex(ord(i))).upper() for i in char])

    @staticmethod
    def decode(char):
        ch = []

        for uni in str(char).split(" "):
            ch.append(chr(int(uni, 16)))
            return "".join(ch)


class MorseCode:
    @staticmethod
    def encode(char: str):
        MorseCode = {
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            " ": f"/ ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
            "0": "----- ",
            ",": "--..-- ",
            ".": ".-.-.- ",
            "?": "..--.. ",
            "-": "-....- ",
            "(": "-.--. ",
            ")": "-.--.- ",
            '"': ".-..-. ",
            "'": ".----. ",
        }
        return char.upper().translate(str.maketrans(MorseCode))

    @staticmethod
    def decode(char: str):
        MorseCode = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            " ": "/",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            "0": "-----",
            ",": "--..--",
            ".": ".-.-.-",
            "?": "..--..",
            "-": "-....-",
            "(": "-.--.",
            ")": "-.--.-",
            '"': ".-..-.",
            "'": ".----.",
        }

        result = char.split(" ")
        ch = []

        while "" in result:
            result.remove("")

        for i in result:
            ch.append(list(MorseCode.keys())[
                      list(MorseCode.values()).index(i)])

        return str("".join(ch)).lower()

