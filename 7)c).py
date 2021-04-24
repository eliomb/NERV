import datetime
def fechavalida():
    """utilizando la libreria de datetime nuevamente, hago uso de un try-except para confirmar si se pudo convertir el dato string a tipo datetime. en ese caso, la variable "valida" queda en true, por lo que se asume que la fecha paso el try-except correctamente. si hay una excepcion, "valida" queda en falso, por ende, al pasar la validacion, nos indica que no es valida."""
    fecha = input("Ingresa una fecha valida (DD/MM/AAAA ): ")

    dia,mes,año = fecha.split('/')

    valida = True
    try:
        datetime.datetime(int(año),int(mes),int(dia))
    except ValueError:
        valida = False

    if valida == True:
        print("La fecha {} es valida.".format(fecha))
    else:
        print("La fecha es invalida, o los datos ingresados no son fechas.")

    
fechavalida()
