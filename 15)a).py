def mayusculas2():
    string = input("Ingresa una palabra: ")
    may = string.split()
    palabra = ""
    iniciales = ""

    
    for x in range(0, len(may)):
        palabra = may[x]
        if may[x] == palabra:
            iniciales += palabra[0].upper()
    print("Las iniciales son: {}".format(iniciales))


    
    return(palabra)


