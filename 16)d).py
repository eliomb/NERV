"""
en esta simplemente creo una funcion que valide si la palabra ingresada es
igual a la palabra dada vuelta. En ese caso, va a devolver True siempre y cuando
tu palabra sea un palindromo. Caso contrario, te indicara que no.
"""

def espalindromo(reverso):
    if reverso == reverso[::-1]: # valida si la palabra es igual a la palabra en reversa
        return True
    else:
        return False

def palindromo():
    reverso = input("Ingresa un palindromo: ").replace(" ","") # remueve los espacios
    validacion = espalindromo(reverso)

    if validacion is True:
        print("Tu palabra {} es un palindromo.".format(reverso))
    else:
        print("Tu palabra {} no es un palindromo.".format(reverso))
    
palindromo()
