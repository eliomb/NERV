"""
las funciones del 15) menos el 15)b) utilizan un for que
recorre la lista de elementos formada por el split(), que
luego usando variables vacias, guarda cada palabra en
la variable A y con un if, elejimos la primera posicion
de la palabra, es decir, la primera letra. Esto lo hara por
cada letra que en la que el for esta parado por la lista.
"""

def soloa():
    string = input("Ingrese una sentencia: ")
    palabra = string.split()
    a = ""
    b = ""


    for x in range(0, len(palabra)):
        a = palabra[x]
        if a[0] in "Aa":
            b += a
        else:
            print("Esta sentencia no tiene palabras que empiecen por 'A'.")
    print("Palabras: {}".format(b))

soloa()
    
