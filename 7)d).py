import datetime
from calendar import monthrange

def fechavalida():
    date = input("Ingresa una fecha valida (DD/MM/AAAA ): ")

    dia,mes,año = date.split('/')

    valida = True
    try:
        datetime.datetime(int(año),int(mes),int(dia))
    except ValueError:
        valida = False

    if valida == True:
        print("La fecha {} es valida.".format(date))
        return date
    else:
        print("La fecha es invalida, o los datos ingresados no son fechas.")
        exit


def findemes():
    """
    en este codigo utilizo una funcion de un ejercicio anterior en el que valido primero
    si la fecha elegida es valida, y luego regresa dicha fecha al terminar la funcion.
    esta misma fecha luego la guardo en una variable en findemes() y luego la convierto
    a datetime con "strptime", para luego guardar en variables cada parte de la fecha que luego
    me sera util para el monthrange, que mide la semana del mes y la cantidad de dias en el mes
    elegido. de ambos valores, solo elijo el de los dias totales en el mes, asi en un try-except
    hago una cuenta rapida.
    """
    date = fechavalida()
    formato = "%d/%m/%Y"
    dateobj = datetime.datetime.strptime(date, formato)
    yearnow = dateobj.year
    monthnow = dateobj.month
    daynow = dateobj.day
    days = monthrange(yearnow, monthnow)[1]
    try:
        daysleft = days - daynow
        print("Faltan {} dias para el fin de mes.".format(daysleft))
    except ValueError:
        print("Error de formato.")


findemes()
    

