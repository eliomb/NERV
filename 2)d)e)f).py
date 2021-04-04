def circuloperim():
    """lo que esta funcion hace es utilizar el calculo del perimetro de un circulo y lo complementa con la variable del usuario y una constante pi"""
    radio = float(input("Introduzca el radio el circulo: "))
    pi = float(3.14159)
    if radio >= 0:
        long = float(2 * pi * radio)
        print("La longitud del perimetro de este circulo es: ", long)
    else:
        print("NO puede ser menor ni igual a cero!")
    """decidi utilizar float por razones muy obvias, es decir, en caso de que se utilicen decimales."""

"circuloperim()"

def circuloarea():
    """en cambio, esta funcion calcula el area en base a su radio"""
    radio = float(input("Introduzca el radio el circulo: "))
    pi = float(3.14159)
    if radio >= 0:
        area = float(pi * pow(radio, 2))
        print("El area de este circulo es: ", area)
    else:
        print("NO puede ser menor ni igual a cero!")

"circuloarea()"

def esferavolumen():
    """en esta, usamos el radio como variable del usuario tambien para poder calcular el volumen de una esfera."""
    radio = float(input("Introduzca el radio el circulo: "))
    pi = float(3.14159)
    if radio >= 0:
        volumen = (4 / 3) * pi * pow(radio, 3)
        print("El volumen de esta esfera es: ", volumen)
    else:
        print("NO puede ser menor ni igual a cero!")

"esferavolumen()"
    
