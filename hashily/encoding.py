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
    def encode(char: str):
        """
        Converts the plain text to a Binary string.
        """
        return " ".join(format(ord(i), '08b') for i in char.strip())

    def decode(char: int):
        """
        Converts the Binary string to a Plain Text.
        """
        return "".join(chr(int(i, 2)) for i in char.strip().split(" "))


class Hexadecimal:
    def encode(char: str):
        """
        Converts the plain text to a Hexadecimal string.
        """
        return " ".join(format(ord(i), 'x') for i in char)

    def decode(char: str):
        """
        Converts the Hexadecimal string to a Plain Text.
        """
        return "".join(chr(int(i, 16)) for i in char.strip().split(" "))


class Octal:
    def encode(char: str):
        """
        Converts the plain text to a Octal string.
        """
        return " ".join(format(ord(i), 'o') for i in char)

    def decode(char: str):
        """
        Converts the Octal string to a Plain Text.
        """
        return "".join(chr(int(i, 8)) for i in char.strip().split(" "))


class Integer:
    def encode(char: str):
        """
        Converts a String to it's ASCII number
        """
        return " ".join(str(ord(i)) for i in char)

    def decode(char):
        """
        Converts the ASCII number to it's Original String
        """
        return "".join(chr(int(i)) for i in str(char).split(" "))


class UrlEncoding:
    def encode(char: str):
        """
        Substitute percent %xx escapes equivalents for single-character.
        """
        return urllib.parse.quote(char)

    def decode(char: str):
        """
        Substitute single-character equivalents for Percent %xx escapes.
        """
        return urllib.parse.unquote(char)


class UnicodePoint:
    def encode(char):
        """
        Converts Plain text to Unicode-Encoded text.
        """
        return " ".join([str(hex(ord(i))) for i in char])

    def decode(char):
        """
        Converts a Unicode-Encoded text to a Plain Text.
        """
        ch = []

        for uni in str(char).split(" "):
            ch.append(chr(int(uni, 16)))

        return "".join(ch)
