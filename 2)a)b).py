def perimetro():
    """Lo que esta funcion hace es pedirte la base y la altura, y luego hace el calculo por ti y te muestra el perimetro."""
    base = int(input("ingrese la base."))
    altura = int(input("ingrese la altura."))
    perimetro = int(base * 2 + altura * 2)
    if altura == base:
        print("Esto es un cuadrado.")
    print("El perimetro es: ", perimetro)

perimetro()


def area():
    """Tiene una estructura parecida al de perimetro, solo que se reemplaza el calculo de perimetro con el de superficie."""
    base = int(input("ingrese la base."))
    altura = int(input("ingrese la altura."))
    area = base * altura
    if altura == base:
        print("Esto es un cuadrado.")
    print("La superficie es: ", area)
"""y ademas te indica si es un cuadrado o no."""
area()
