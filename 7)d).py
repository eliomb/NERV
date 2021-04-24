import datetime
from calendar import monthrange


def findemes():
    """nuevamente uso las librerias calendar y datetime para hacer un programa que mide los dias que faltan hasta fin de mes utilizando "monthrange" de calendar. esto basicamente nos dice la semana en la que estamos y los dias totales del mes, y usando ese valor, guardo en una variable los dias totales del mes actual, y en otra variable guardo el dia actual. luego, para evitar errores, utilizo un try-except para meter una cuenta rapida, y automaticamente hace el calculo sin necesidad de algun input"""
    fecha = datetime.datetime.now()
    yearnow = fecha.year
    monthnow = fecha.month
    daynow = fecha.day
    days = monthrange(yearnow, monthnow)[1]
    try:
        daysleft = days - daynow
        print("Faltan {} dias para el fin de mes.".format(daysleft))
    except ValueError:
        print("Error de formato.")
    


findemes()
