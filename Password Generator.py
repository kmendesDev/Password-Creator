import random
import string


def Password_creation():
    UpperCase = string.ascii_uppercase
    LowerCase = string.ascii_lowercase
    Numbers = "123456789"
    Symbols = "[]{}()*;/,_-"
    JoinAll = UpperCase + LowerCase + Numbers + Symbols
    Length = int(input("Digite o tamanho da senha desejada: "))

    Password = "".join(random.sample(JoinAll, Length))
    print("Sua senha é: " + Password)


Password_creation()
