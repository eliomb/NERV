
def vocales():
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
