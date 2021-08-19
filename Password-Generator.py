# This is a password generator that creates random passwords
# don't forget to install required packages you can install
# python packages using 'pip install <package>' command.

import random

lcletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ucletters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", ";", ":"]

rndmlclttrs = random.choices(lcletters, k=5)
rndmuclttrs = random.choices(ucletters, k=5)
rndmnmbrs = random.choices(numbers, k=5)
rndmsymbls = random.choices(symbols, k=5)

newlist = rndmlclttrs + rndmuclttrs + rndmnmbrs + rndmsymbls

password = random.choices(newlist, k=20)
print(password)

def convert(password):
    new = ""

    for x in password:
        new += x
    return new

print("Password : ",convert(password))
