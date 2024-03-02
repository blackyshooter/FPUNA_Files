import os;
import random;

def clear():
    ''''LIMPIA LA PANTALLA'''
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("Adivina mi numero")
limite = 5
number = random.randint(1,limite)

c=0
print("ESTOY PENSANDO EN UN NUMERO DEL 1 AL ",limite)

while True:
    result = int(input("CUAL CREES  QUE ES "))
    c+=1
    if result == number:
        print("¡Felicidades! ¡Has adivinado el número en", c, "intentos!")
        break
    elif result > number:
        print("MI NUMERO ES MENOR")
    else:
         print("MI NUMERO ES MAYOR")


