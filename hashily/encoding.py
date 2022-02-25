import utils
import urllib.parse


class Binary:
    @staticmethod
    def encode(char: str):
        """
        Returns the Binary Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        binary_text : str
            The encrypted text.
        """
        binary_text = " ".join(format(ord(i), "08b") for i in char.strip())

        return binary_text

    @staticmethod
    def decode(char: int):
        """
        Returns the decrypted text for Binary.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        binary_translated : str
            The decrypted text.
        """

        if " " not in char and len(char) > 8:
            raise utils.exceptions.NoSpaceError(char)

        binary_translated = "".join(chr(int(i, 2)) for i in char.strip().split(" "))

        return binary_translated


class Hexadecimal:
    @staticmethod
    def encode(char: str):
        """
        Returns the Hexadecimal Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        hexadecimal_text : str
            The encrypted text.
        """
        hexadecimal_text = " ".join(format(ord(i), "x") for i in char)

        return hexadecimal_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for Hexadecimal.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        hexadecimal_translated : str
            The decrypted text.
        """

        if " " not in char and len(char) > 2:
            raise utils.exceptions.NoSpaceError(char)

        hexadecimal_translated = "".join(
            chr(int(i, 16)) for i in char.strip().split(" ")
        )

        return hexadecimal_translated


class Octal:
    @staticmethod
    def encode(char: str):
        """
        Returns the Octal Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        octal_text : str
            The encrypted text.
        """
        octal_text = " ".join(format(ord(i), "o") for i in char)

        return octal_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for Octal.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        octal_translated : str
            The decrypted text.
        """
        if " " not in char and len(char) > 3:
            raise utils.exceptions.NoSpaceError(char)

        octal_translated = "".join(chr(int(i, 8)) for i in char.strip().split(" "))

        return octal_translated


class ASCII:
    @staticmethod
    def encode(char: str):
        """
        Returns the ASCII Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        ascii_text : str
            The encrypted text.
        """
        ascii_text = " ".join(str(ord(i)) for i in char)

        return ascii_text

    @staticmethod
    def decode(char):
        """
        Returns the decrypted text for ASCII.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        ascii_translated : str
            The decrypted text.
        """
        if " " not in char:
            raise utils.exceptions.NoSpaceError(char)

        ascii_translated = "".join(chr(int(i)) for i in str(char).split(" "))

        return ascii_translated


class UrlEncoding:
    @staticmethod
    def encode(char: str):
        """
        Returns the URL Encoding Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        urlencoding_text : str
            The encrypted text.
        """
        urlencoding_text = urllib.parse.quote(char)

        return urlencoding_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for URL Encoding.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        urlencoding_translated : str
            The decrypted text.
        """
        urlencoding_translated = urllib.parse.unquote(char)

        return urlencoding_translated


class UnicodePoint:
    @staticmethod
    def encode(char: str):
        """
        Returns the Unicode Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        unicode_text : str
            The encrypted text.
        """
        unicode_text = " ".join([str(hex(ord(i))) for i in char])

        return unicode_text

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for Unicode.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        unicode_translated : str
            The decrypted text.
        """
        unicode_translated = "".join(
            [chr(int(uni, 16)) for uni in str(char).split(" ")]
        )

        return unicode_translated


class Base32:
    @staticmethod
    def encode(char: str):
        """
        Returns the Pure Base32 Translation of the text.

        Parameters
        ----------
        char : str
            The text needs to be encrypted.

        Returns
        -------
        base32_text : str
            The encrypted text.
        """
        base32_text = []

        for texts in [char[i : i + 5] for i in range(0, len(char), 5)]:

            ascii = [ord(s) for s in texts]
            binary = ["{0:08b}".format(s) for s in ascii]
            group_five = [0, 0, 0, 0, 0]

            for i in range(5):
                try:
                    group_five[i] = binary[i]
                except IndexError:
                    group_five[i] = "xxxxxxxx"

            five_split = ["".join(group_five)[s : s + 5] for s in range(0, 40, 5)]
            clean = []

            for s in five_split:
                if s and ("0" in s or "1" in s):
                    clean.append(s.replace("x", "0"))
                else:
                    clean.append(s)
            clean_with_pads = ["=" if s == "xxxxx" else s for s in clean]
            decimal = [int(s, 2) if s.isdigit() else s for s in clean_with_pads]
            base32 = "".join([utils.constants.characters[str(s)] for s in decimal])

            base32_text.append(base32)

        return "".join(base32_text)

    @staticmethod
    def decode(char: str):
        """
        Returns the decrypted text for Base32.

        Parameters
        ----------
        char : str
            The text that needs to be decrypted.

        Returns
        --------
        base32_translated : str
            The decrypted text.
        """
        base32_translated = []

        for texts in [char[i : i + 8] for i in range(0, len(char), 8)]:
            unbase32 = [
                {value: key for key, value in utils.constants.characters.items()}[s]
                for s in list(texts)
            ]
            dec_to_bin = [
                "xxxxx" if s == "=" else "{0:05b}".format(int(s)) for s in unbase32
            ]

            five_to_eight = ["".join(dec_to_bin)[i : i + 8] for i in range(0, 40, 8)]
            clean = []

            for s in five_to_eight:
                if s and "x" in s:
                    clean.append(s.replace("0", "x").replace("1", "x"))
                else:
                    clean.append(s)
            remove_x = [s for s in clean if s != "xxxxxxxx"]
            bin_to_dec = [int(s, 2) for s in remove_x]
            dec_to_ascii = [chr(int(i)) for i in bin_to_dec]

            base32_translated.append("".join(dec_to_ascii))

        return "".join(base32_translated)
