import random
import string
import secrets


def password(length: int = 16):
    """
    Creates a secure password of the specified length.
    """
    foobar = []
    chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(chars)

    try:
        if length > 16:
            raise ValueError("The password can be no longer than 16 characters and no shorter than eight characters.")
        
        elif length < 8:
            raise ValueError("The password can be no longer than 16 characters and no shorter than eight characters.")

        else:
            for i in range(length):
                foobar.append(random.choice(chars))

            return "".join(foobar)
    
    except Exception as e:
        raise e


def token():
    """
    Returns a Strong Random Text Token in Hexadecimal
    """
    alphabet = string.ascii_letters + string.digits

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(48))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


def reverse(text: str):
    """
    Returns the string in reverse order.
    """
    return text[::-1]


def titleize(text: str):
    """
    Capitalizes all the words in a String
    """
    return " ".join(i.strip().lower().capitalize() for i in text.split())


