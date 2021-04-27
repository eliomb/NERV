
def vocales():

    """
    un for recorre la palabra y revisa si alguna de las palabras en las que esta
    el for coincide con una de las palabras en el string "aeiouAEIOU", que
    contiene a todas las vocales en minusculas y mayusculas, y en base a eso
    le suma 1 a la variable vocal, que cuenta la cantidad de vocales que hay en
    el string ingresado.
    """
    
    palabra = input("Ingresa una palabra: ")
    vocal = 0

    for i in palabra:
        if i in "aeiouAEIOU":
            vocal += 1

    if vocal > 0:
        print("La palabra {} tiene {} vocales.".format(palabra, vocal))
    else:
        print("Esta palabra no tiene vocales.")



vocales()
