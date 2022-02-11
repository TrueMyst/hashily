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
            raise ValueError(
                "The password can be no longer than 16 characters and no shorter than eight characters.")

        elif length < 8:
            raise ValueError(
                "The password can be no longer than 16 characters and no shorter than eight characters.")

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


def altCase(text: str):
    """
    Returns an Alternate Casing of the Text
    """
    return "".join([words.upper() if index % 2 else words.lower() for index, words in enumerate(text)])
