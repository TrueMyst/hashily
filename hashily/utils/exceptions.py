from pyclbr import Function
from colorama import Fore

class NoSpaceError(Exception):
    """Raised when there is no space in the given Text"""
    def __init__(self, text):
        self.text = text
        self.message = f"There were no spaces identified in the Variable's Value | Value: \"{self.text}\""
        super().__init__(self.message)

class CharLengthShort(Exception):
    """Raised when the length of the'Char' doesn't matches with the base """
    def __init__(self, Class, Function, CharLen: int):
        self.message = f"The 'char' received a very short length. The {Class}'s {Function}: Requires a length of {CharLen}."
        super().__init__(self.message)


def CustomValueError(Class: str, Func: str, Param):
    return f"{Fore.RED}[x] " f"{Fore.BLUE}[{Class}: {Func}] - " f"{Fore.RED}'{Param}' is not a positive number. {Fore.RESET}"

