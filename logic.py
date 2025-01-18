import random as r, string as s, discord, os


def password(length):
    elements = s.ascii_letters+s.ascii_uppercase+s.digits+s.punctuation

    password = ""

    for i in range(length):
        password += r.choice(elements)
    return password

def elegir(choices):
    return r.choice(choices)

def meme():
    with open("img/meme 1.jpeg","rb") as m:
        picture = discord.File(m)
    return picture

def memes():
    meme_ran = r.choice(os.listdir("img"))
    with open(f"img/{meme_ran}","rb") as m:
        picture = discord.File(m)
    return picture