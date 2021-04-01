def saludo():
    """esta funcion utiliza un user input, y luego valido con un if en caso de que pueda estar vacia."""
    print("Cual es tu nombre?")
    nombre = input()
    if nombre != "":
        print("Hola, " + nombre + "!")

saludo()
