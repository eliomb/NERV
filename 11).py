def calificaciones():

    """
    lo que esta funcion utiliza es una regla de 3 dentro de un for para resolver
    el calculo de porcentaje, y el problema entero es resuelto adentro de un for
    que forma a los resultados como si fuera una tabla de resultados. en el
    caso de que hayan respuestas mayores a la cantidad de ejercicios totales,
    el programa asume que es un error de calificacion y no muestra ese
    resultado en especifico, continuando con los que estan bien.
    """
    ejer = int(input("Ingresa la cantidad de ejercicios totales: "))
    listaexamen = [
        (int(input("Resueltos:")), ejer),
        (int(input("Resueltos:")), ejer),
        (int(input("Resueltos:")), ejer),
        (int(input("Resueltos:")), ejer),
        (int(input("Resueltos:")), ejer)]
    print(listaexamen)

    res = 0
    por = 0
    cantidad = 1
    
    for i, x in listaexamen:
        if i < x:
            res = i
            por = float((res / ejer) * 100)
            if por >= 60:
                print("Calificacion examen num. {}: {}% | APROBADO | {} de {} ejercicios resueltos.".format(cantidad, por, i , x))
            else:
                print("Calificacion examen num. {}: {}% | DESAPROBADO | {} de {} ejercicios resueltos. ".format(cantidad, por, i, x))
        else:
            print("Error de ingreso. Vuelva a ingresar los datos.")
            exit
        cantidad += 1



calificaciones()
    
