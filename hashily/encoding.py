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


class Binary:
    @staticmethod
    def encode(char: str):
        """
        Converts the plain text to a Binary string.
        """
        return " ".join(format(ord(i), "08b") for i in char.strip())

    @staticmethod
    def decode(char: int):
        """
        Converts the Binary string to a Plain Text.
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
        Converts a String to it's ASCII number
        """
        return " ".join(str(ord(i)) for i in char)

    @staticmethod
    def decode(char):
        """
        Converts the ASCII number to it's Original String
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
        characters = {
            "0": "A",
            "1": "B",
            "2": "C",
            "3": "D",
            "4": "E",
            "5": "F",
            "6": "G",
            "7": "H",
            "8": "I",
            "9": "J",
            "10": "K",
            "11": "L",
            "12": "M",
            "13": "N",
            "14": "O",
            "15": "P",
            "16": "Q",
            "17": "R",
            "18": "S",
            "19": "T",
            "20": "U",
            "21": "V",
            "22": "W",
            "23": "X",
            "24": "Y",
            "25": "Z",
            "26": "2",
            "27": "3",
            "28": "4",
            "29": "5",
            "30": "6",
            "31": "7",
            "=": "=",
        }

        result = []

        for texts in [char[i : i + 5] for i in range(0, len(char), 5)]:
            ASCII = [ord(s) for s in texts]
            Binary = ["{0:08b}".format(s) for s in ASCII]
            GroupFive = [0, 0, 0, 0, 0]

            for i in range(5):
                try:
                    GroupFive[i] = Binary[i]
                except IndexError:
                    GroupFive[i] = "xxxxxxxx"

            FiveSplit = ["".join(GroupFive)[s : s + 5] for s in range(0, 40, 5)]
            clean = []

            for s in FiveSplit:
                if s:
                    if "0" in s or "1" in s:
                        clean.append(s.replace("x", "0"))
                    else:
                        clean.append(s)
                else:
                    clean.append(s)

            CleanWithPads = ["=" if s == "xxxxx" else s for s in clean]
            Decimal = [int(s, 2) if s.isdigit() else s for s in CleanWithPads]
            Base32 = "".join([characters[str(s)] for s in Decimal])

            result.append(Base32)

        return "".join(result)

    @staticmethod
    def decode(char: str):
        result = []

        for texts in [char[i : i + 8] for i in range(0, len(char), 8)]:
            characters = {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3",
                "E": "4",
                "F": "5",
                "G": "6",
                "H": "7",
                "I": "8",
                "J": "9",
                "K": "10",
                "L": "11",
                "M": "12",
                "N": "13",
                "O": "14",
                "P": "15",
                "Q": "16",
                "R": "17",
                "S": "18",
                "T": "19",
                "U": "20",
                "V": "21",
                "W": "22",
                "X": "23",
                "Y": "24",
                "Z": "25",
                "2": "26",
                "3": "27",
                "4": "28",
                "5": "29",
                "6": "30",
                "7": "31",
                "=": "=",
            }
            l = [s for s in texts]

            UnBase32 = [characters[s] for s in l]
            DecToBin = [
                "xxxxx" if s == "=" else "{0:05b}".format(int(s)) for s in UnBase32
            ]

            FiveToEight = ["".join(DecToBin)[i : i + 8] for i in range(0, 40, 8)]
            clean = []

            for s in FiveToEight:
                if s:
                    if "x" in s:
                        clean.append(s.replace("0", "x").replace("1", "x"))
                    else:
                        clean.append(s)
                else:
                    clean.append(s)

            RemoveX = [s for s in clean if s != "xxxxxxxx"]
            BinToDec = [int(s, 2) for s in RemoveX]
            DecToASCII = [chr(int(i)) for i in BinToDec]

            result.append("".join(DecToASCII))

        return "".join(result)
