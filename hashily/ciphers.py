import utils


class ROT13:
    @staticmethod
    def encode(char: str):
        """
        Returns the ROT13 translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        ROT13_text: str
            The encrypted text.
        """
        ROT13_text = char.translate(
            bytes.maketrans(
                bytes(utils.constants.upper + utils.constants.lower, "utf-8"),
                bytes(
                    utils.constants.upper[13:]
                    + utils.constants.upper[:13]
                    + utils.constants.lower[13:]
                    + utils.constants.lower[:13],
                    "utf-8",
                ),
            )
        )

        return ROT13_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for the AtBash cipher.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        ROT13_translated: str
            The decrypted text.
        """
        ROT13_translated = char.translate(
            bytes.maketrans(
                bytes(
                    utils.constants.upper[13:]
                    + utils.constants.upper[:13]
                    + utils.constants.lower[13:]
                    + utils.constants.lower[:13],
                    "utf-8",
                ),
                bytes(utils.constants.upper + utils.constants.lower, "utf-8"),
            )
        )

        return ROT13_translated


class AtBash:
    @staticmethod
    def encode(char: str):
        """
        Returns the AtBash translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        Atbash_text: str
            The encrypted text.
        """
        Atbash_text = ""

        for letters in char:
            if letters.isupper():
                Atbash_text += chr((ord("Z") + ord("A")) - ord(letters))

            elif letters.islower():
                Atbash_text += chr(ord("z") + ord("a") - ord(letters))

            else:
                Atbash_text += letters

        return Atbash_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for the AtBash cipher.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        -------
        Atbash_translated: str
            The decrypted text.
        """
        Atbash_translated = ""

        for letters in char:
            if letters.isupper():
                Code = ord("Z") + ord("A")
                Atbash_translated += chr(Code - ord(letters))

            elif letters.islower():
                Code = ord("z") + ord("a")
                Atbash_translated += chr(Code - ord(letters))
            else:
                Atbash_translated += letters

        return Atbash_translated


class Bacon:
    @staticmethod
    def encode(char: str):
        """
        Returns the Bacon translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        Bacon_text: str
            The encrypted text.
        """
        Bacon_text = char.upper().translate(str.maketrans(utils.constants.BaconDict))

        return Bacon_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for the Bacon cipher.

        Parameters
        ----------
        char : str
            The text needs to be decrypted.

        Returns
        -------
        Bacon_translated: str
            The decrypted text.
        """
        Bacon_translated = ""
        i = 0
        while True:
            if i >= len(char) - 4:
                break

            sets = char[i : i + 5]
            if sets[0] != " ":
                Bacon_translated += list(utils.constants.BaconDict.keys())[
                    list(utils.constants.BaconDict.values()).index(sets)
                ].lower()
                i += 5
            else:
                Bacon_translated += " "
                i += 1

        return Bacon_translated


class A1Z26:
    @staticmethod
    def encode(char: str):
        """
        Returns the A1Z26 translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        A1Z26_text: str
            The encrypted text.
        """
        A1Z26_text = []
        for i in char:
            if i.isalpha():
                A1Z26_text.append(str(ord(i.lower()) - 96))
            else:
                A1Z26_text.append(i)
        for i in range(len(A1Z26_text)):
            if A1Z26_text[i] == " ":
                A1Z26_text[i] = ""

        return " ".join(A1Z26_text)

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for the A1Z26 cipher.

        Parameters
        ---------
        char : str
            The text needs to be decrypted.

        Returns
        -------
        A1Z26_translated: str
            The decrypted text.
        """
        A1Z26_translated = []

        for i in char.split(" "):
            if i != "":
                A1Z26_translated.append(chr(int(i) + 96))
            else:
                A1Z26_translated.append(" ")

        return "".join(A1Z26_translated)


class Caesar:
    @staticmethod
    def encode(char: str, shift: int = 3):
        """
        Returns the Caesar translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.
        shift : int, optional
            The shift that needs be applied to the text in order to encrypt it. Defaults to 3.

        Returns
        -------
        Caesar_text: str
            The encrypted text.
        """

        Caesar_text = ""
        for i in range(len(char)):
            if char[i].isupper():
                Caesar_text += chr((ord(char[i]) + shift - 65) % 26 + 65)

            elif char[i].islower():
                Caesar_text += chr((ord(char[i]) + shift - 97) % 26 + 97)
            else:
                Caesar_text += char[i]

        return Caesar_text

    @staticmethod
    def decode(char: str, shift: int = 3):
        """
        Returns the decrypted text for the Caesar cipher.

        Parameters
        ----------
        char : str
            The text needs to be decrypted.
        shift : int, optional
            The shift that needs be applied to the text in order to decrypt it. Defaults to 3.

        Returns
        -------
        Caesar_translated: str
            The decrypted text.
        """
        Caesar_translated = ""

        for i in range(len(char)):
            if char[i].isupper():
                Caesar_translated += chr((ord(char[i]) - shift - 65) % 26 + 65)
            elif char[i].islower():
                Caesar_translated += chr((ord(char[i]) - shift - 97) % 26 + 97)
            else:
                Caesar_translated += char[i]

        return Caesar_translated


class MorseCode:
    @staticmethod
    def encode(char: str):  # sourcery skip: inline-immediately-returned-variable
        """
        Returns the Morse Code translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        MorseCode_text: str
            The encrypted text.
        """
        MorseCode_text = "".join(
            f"{utils.constants.MorseCodeDict[i]} " if i != " " else "/ "
            for i in char.upper()
        )

        return MorseCode_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for the MorseCode cipher.

        Parameters
        ----------
        char : str
            The text needs to be decrypted.

        Returns
        -------
        MorseCode_translated: str
            The decrypted text.
        """
        char += " "
        MorseCode_translated = ""
        containIT = ""

        for i in char:
            if i != " ":
                counter = 0
                containIT += i

            else:
                counter += 1

                if counter == 2:
                    MorseCode_translated += " "

                else:
                    MorseCode_translated += list(utils.constants.MorseCodeDict.keys())[
                        list(utils.constants.MorseCodeDict.values()).index(containIT)
                    ]
                    containIT = ""

        return MorseCode_translated
