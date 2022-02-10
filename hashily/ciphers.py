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
 
import utils


class ROT12:
    def encode(char: str):
        return char.translate(bytes.maketrans(bytes(utils.upper+utils.lower,"utf-8"), bytes(utils.upper[13:]+utils.upper[:13]+utils.lower[13:]+utils.lower[:13],"utf-8")))

    def decode(char: str):
        return char.translate(bytes.maketrans(bytes(utils.upper[13:]+utils.upper[:13]+utils.lower[13:]+utils.lower[:13],"utf-8"), bytes(utils.upper+utils.lower,"utf-8")))



class AtBash:

    def encode(char):
        AtBash = ""

        for letters in char:
            if letters.isupper():
                AtBash += chr((ord('Z') + ord('A')) - ord(letters))

            elif letters.islower():
                AtBash += chr(ord('z') + ord('a') - ord(letters))

            else:
                AtBash += letters

        return AtBash

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


class Bacon:
    def encode(char: str):
        return char.utils.upper().translate(str.maketrans(utils.tempvar.BaconDict))

    def decode(char: str):
        BaconText = ''
        i = 0
        while True:
            if(i < len(char)-4):
                sets = char[i:i + 5]
                if sets[0] != ' ':
                    BaconText += list(utils.tempvar.BaconDict.keys())[list(
                        utils.tempvar.BaconDict.values()).index(sets)].utils.lower()
                    i += 5
                else:
                    BaconText += ' '
                    i += 1
            else:
                break


class A1Z26:
    def encode(char: str):
        A1Z26 = []

        for i in char:
            if i.isalpha():
                A1Z26.append(str(ord(i.utils.lower()) - 96))

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


class Caesar:

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


class MorseCode:
    def encode(char: str):
        MorseCodeText = ""

        for i in char.utils.upper():
            if i != " ":
                MorseCodeText += utils.tempvar.MorseCodeDict[i] + " "

            else:
                MorseCodeText += "/ "

        return MorseCodeText

    def decode(char: str):
        char += ' '
        decipher = ''
        containIT = ''

        for i in char:
            if (i != ' '):
                counter = 0
                containIT += i

            else:
                counter += 1
                if counter == 2:
                    decipher += ' '

                else:
                    decipher += list(utils.tempvar.MorseCodeDict.keys())[list(utils.tempvar.MorseCodeDict.values()).index(containIT)]
                    containIT = ''

        return decipher
