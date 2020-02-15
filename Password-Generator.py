import random

lcletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ucletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", ";", ":"]

rndmlclttrs = random.choices(lcletters, k=3)
rndmuclttrs = random.choices(ucletters, k=3)
rndmnmbrs = random.choices(numbers, k=3)
rndmsymbls = random.choices(symbols, k=3)

newlist = rndmlclttrs + rndmuclttrs + rndmnmbrs + rndmsymbls

password = random.choices(newlist, k=12)

def convert(password):
    new = ""

    for x in password:
        new += x
    return new

print("Password : ",convert(password))
