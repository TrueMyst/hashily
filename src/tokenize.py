import random
import string


def hashed(length: int = 16):
    chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(chars)

    foobar = []

    try:
        if length > 16:
            return "The Password can be no longer than 16 and no shorter than eight characters"

        else:
            for i in range(length):
                foobar.append(random.choice(chars))

            return "".join(foobar)

    except:
        pass


def token(length: int = 59):
    chars = list(string.ascii_letters + "-._" + string.digits)
    random.shuffle(chars)

    foobar = []

    for i in range(length):
        foobar.append(random.choice(chars))

    random.shuffle(foobar)

    return "".join(foobar)


