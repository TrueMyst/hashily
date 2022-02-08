from Utils import exceptions

class ASCII():
    @staticmethod
    def encode(char: str):
        return " ".join(format(ord(i)) for i in char)


    @staticmethod
    def decode(char: str):
        return "".join(format(chr(int(i))) for i in char.strip().split())


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
        BaconDict = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
                    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
                    'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
                    'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
                    'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 
                    'Z':'bbaab'}

        return char.upper().translate(str.maketrans(BaconDict))

    def decode(char: str):
        BaconDict = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
                    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
                    'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
                    'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
                    'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 
                    'Z':'bbaab'}
        
        BaconDictReversed = {keys:values for keys,values in BaconDict.items()}


        Bacon = ""

        i = 0

        while True:

            if i < len(char) -4:
                letters= char[i:i+5]

                if letters[0]!=' ':
                    Bacon += BaconDictReversed[letters] + " "
                    i+=5

                else:
                    Bacon += " "
                    i+=1
            else:
                break

        return Bacon

print(Bacon.encode("Hello World"))