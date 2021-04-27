def comparacion():
    palabra1 = input("Dame una palabra: ")
    palabra2 = input("Dame otra palabra: ")
    verdadero = False
    if palabra1 == palabra2.upper(): 
        verdadero = True
        print("Es la primera palabra es la mayuscula de la segunda? {}".format(verdadero))
    elif palabra1.upper() == palabra2:
        verdadero = False
        print("Es la primera palabra es la mayuscula de la segunda? {}".format(verdadero))


comparacion()
