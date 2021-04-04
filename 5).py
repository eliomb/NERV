def temperaturas(fah):
    """esta funcion simplemente convierte de fahrenheit a celsius"""
    "fah = float(input(Ingresa una temperatura en fahrenheit: ))"
    cel = (fah - 32) * 5/9
    print(fah," °F |", cel, " °C")

def tabla():
    """la funcion tabla iguala la variable 'fah' a 'i' en el momento en el que se invoca en el FOR, y usando un IF verificamos con un modulo si i es multiplo de 10, efectivamente haciendo que la funcion temperaturas imprima nada mas aquellos valores multiplos de 10."""
    for i in range(0, 121):
        if i % 10 == 0:
            temperaturas(i)
        

tabla()

