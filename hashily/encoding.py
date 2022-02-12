"""
MIT License

Copyright (c) 2022 DevMysT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import urllib.parse
from hashily import utils


class Binary:
    @staticmethod
    def encode(char: str):
        """
        Converts the plain text to a binary string.
        """
        return " ".join(format(ord(i), "08b") for i in char.strip())

    @staticmethod
    def decode(char: int):
        """
        Converts the binary string to a Plain Text.
        """
        return "".join(chr(int(i, 2)) for i in char.strip().split(" "))


class Hexadecimal:
    @staticmethod
    def encode(char: str):
        """
        Converts the plain text to a Hexadecimal string.
        """
        return " ".join(format(ord(i), "x") for i in char)

    @staticmethod
    def decode(char: str):
        """
        Converts the Hexadecimal string to a Plain Text.
        """
        return "".join(chr(int(i, 16)) for i in char.strip().split(" "))


class Octal:
    @staticmethod
    def encode(char: str):
        """
        Converts the plain text to a Octal string.
        """
        return " ".join(format(ord(i), "o") for i in char)

    @staticmethod
    def decode(char: str):
        """
        Converts the Octal string to a Plain Text.
        """
        return "".join(chr(int(i, 8)) for i in char.strip().split(" "))


class Integer:
    @staticmethod
    def encode(char: str):
        """
        Converts a String to it's ascii number
        """
        return " ".join(str(ord(i)) for i in char)

    @staticmethod
    def decode(char):
        """
        Converts the ascii number to it's Original String
        """
        return "".join(chr(int(i)) for i in str(char).split(" "))


class UrlEncoding:
    @staticmethod
    def encode(char: str):
        """
        Substitute percent %xx escapes equivalents for single-character.
        """
        return urllib.parse.quote(char)

    @staticmethod
    def decode(char: str):
        """
        Substitute single-character equivalents for Percent %xx escapes.
        """
        return urllib.parse.unquote(char)


class UnicodePoint:
    @staticmethod
    def encode(char: str):
        """
        Converts Plain text to Unicode-Encoded text.
        """
        return " ".join([str(hex(ord(i))) for i in char])

    @staticmethod
    def decode(char: str):
        """
        Converts a Unicode-Encoded text to a Plain Text.
        """
        ch = []
        for uni in str(char).split(" "):
            ch.append(chr(int(uni, 16)))
        return "".join(ch)


class Base32:
    @staticmethod
    def encode(char: str):
        result = []

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
                if s:
                    if "0" in s or "1" in s:
                        clean.append(s.replace("x", "0"))
                    else:
                        clean.append(s)
                else:
                    clean.append(s)

            clean_with_pads = ["=" if s == "xxxxx" else s for s in clean]
            decimal = [int(s, 2) if s.isdigit() else s for s in clean_with_pads]
            base32 = "".join([utils.constants.characters[str(s)] for s in decimal])

            result.append(base32)

        return "".join(result)

    @staticmethod
    def decode(char: str):
        result = []

        for texts in [char[i : i + 8] for i in range(0, len(char), 8)]:
            l = [s for s in texts]

            unbase32 = [
                {value: key for key, value in utils.constants.characters.items()}[s]
                for s in l
            ]
            dec_to_bin = [
                "xxxxx" if s == "=" else "{0:05b}".format(int(s)) for s in unbase32
            ]

            five_to_eight = ["".join(dec_to_bin)[i : i + 8] for i in range(0, 40, 8)]
            clean = []

            for s in five_to_eight:
                if s:
                    if "x" in s:
                        clean.append(s.replace("0", "x").replace("1", "x"))
                    else:
                        clean.append(s)
                else:
                    clean.append(s)

            remove_x = [s for s in clean if s != "xxxxxxxx"]
            bin_to_dec = [int(s, 2) for s in remove_x]
            dec_to_ascii = [chr(int(i)) for i in bin_to_dec]

            result.append("".join(dec_to_ascii))

        return "".join(result)
