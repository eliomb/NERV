from random import randrange

def adivinanzas():
    secreto = randrange(1,1000)
    numero = int(input("Adivina el numero: "))

    while numero > 0:
        if numero > secreto:
            numero = int(input("Tu numero es mayor a el numero secreto. Intenta otra vez: "))
        elif numero < secreto:
            numero = int(input("Tu numero es menor a el numero secreto. Intenta otra vez: "))

        if numero == secreto:
            print("Adivinaste! El numero es: {}".format(secreto))
            break


adivinanzas()
