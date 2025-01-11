import random as r, string as s


def password(length):
    elements = s.ascii_letters+s.ascii_uppercase+s.digits+s.punctuation

    password = ""

    for i in range(length):
        password += r.choice(elements)
    return password

def elegir(choices):
    return r.choice(choices)
