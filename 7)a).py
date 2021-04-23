def bisiesto():
    """lo que este codigo hace es simple, le pide al usuario un año razonable, y mide si es bisiesto o no por medio de modulos."""
    año = input("Ingrese el año: ")
    if len(año) > 5:
        print("Ingrese una fecha mas cercana.")
    if int(año) % 4 == 0 or int(año) % 400 == 0 and int(año) % 100 > 0:
        print("El año {} es bisiesto.".format(año))
    else:
        print("El año {} no es bisiesto.".format(año))

bisiesto()
