"""
    al igual que con el ejercicio de consonantes anterior, hago lo mismo pero
    con una lista de vocales.
"""


def mostrarvocales():
    palabra = input("Ingrese una sentencia: ")
    vocales = ""
    
    for x in range(0, len(palabra)):    # recorre la palabra
        if palabra[x] in "aeiouAEIOU":
            vocales += palabra[x]  # le suma las vocales de nuestra palabra a la nueva palabra
        
    print(vocales)

mostrarvocales()
