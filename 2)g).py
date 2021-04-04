import math

def pitagoras():
    a = float(input("Valor del cateto A: "))
    b = float(input("Valor del cateto B: "))
    if b and a > 0:
        h = math.sqrt(pow(a, 2) + pow(b, 2))
        print("El valor de la hipotenusa es ", h)
    else:
        print("Ningun cateto puede ser negativo.")
        return

pitagoras()
