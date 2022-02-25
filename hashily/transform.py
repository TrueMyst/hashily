import random
import string
import secrets


def password(length: int = 16):
    """
    Creates a secure password of the specified length.

    Parameters
    ----------
    length: int
        The length of the password should be.

    Raises
    ------
    ValueError
        If the password is less than 8 or more than 16 characters long.

    Returns
    -------
    password: str
        The Password that was generated
    """
    password = []
    chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(chars)

    try:
        if length > 16 or length < 8:
            raise ValueError(
                "The password can be no longer than 16 characters and no shorter than eight characters."
            )
        password.extend(random.choice(chars) for _ in range(length))
        return "".join(password)
    except Exception as e:
        raise e from e


def token():
    """
    Generates a Random hex token.

    Returns
    -------
    hex_token : str
        The token that was created.
    """
    alphabet = string.ascii_letters + string.digits

    while True:
        hex_token = "".join(secrets.choice(alphabet) for _ in range(48))
        if (
            any(c.islower() for c in hex_token)
            and any(c.isupper() for c in hex_token)
            and sum(c.isdigit() for c in hex_token) >= 3
        ):
            break

    return hex_token


def reverse(text: str):
    """
    Returns the `text` in reverse order.
    """
    return text[::-1]


def titleize(text: str):
    """
    Capitalizes all the words in the `text`.
    """
    return " ".join(i.strip().lower().capitalize() for i in text.split())


def altCase(text: str):
    """
    Returns an Alternate Casing of the `text`.
    """
    return "".join(
        [
            words.upper() if index % 2 else words.lower()
            for index, words in enumerate(text)
        ]
    )


def firstLetter(text: str):
    """
    Returns the first letter of every word in the `text`.
    """
    return "".join(letter[0] for letter in text.split())


def pigLatin(text: str):
    """
    Returns the Pig Latin translation of the text.
    """
    return "".join(
        f"{word}ay " if word[0] in list("aeiouAEIOU") else word[1:] + word[0] + "ay "
        for word in text.split()
    )
