from calendar import monthrange
from datetime import date
from dateutil import relativedelta
import datetime

"""
    usando la libreria dateutil para sacar relativedelta,
    simplemente medi la diferencia entre ambas fechas ingresadas
    por medio de un dato de tipo delta, que contiene la diferencia
    de tiempo entre las dos fechas.
"""

def fechavalida():
    date1 = input("Ingresa una fecha valida (DD/MM/AAAA ): ")
    date2 = input("Ingresa una segunda fecha: ")

    dia1,mes1,año1 = date1.split('/')
    dia2,mes2,año2 = date2.split('/')

    valida = True
    try:
        datetime.datetime(int(año1),int(mes1),int(dia1))
        datetime.datetime(int(año2),int(mes2),int(dia2))
    except ValueError:
        valida = False

    if valida == True:
        print("Las fechas {} y {} son validas.".format(date1,date2))
        return date1,date2
    else:
        print("La fecha es invalida, o los datos ingresados no son fechas.")
        exit

def diasaño():
    date1,date2 = fechavalida()
    formato = "%d/%m/%Y"
    fecha1 = datetime.datetime.strptime(date1, formato)
    fecha2 = datetime.datetime.strptime(date2, formato)
    try:
        diferencia = relativedelta.relativedelta(fecha1,fecha2)
        años = diferencia.years
        meses = diferencia.months
        dias = diferencia.days
        print("Hay {} años, {} meses y {} dias entre las fechas.".format(años,meses,dias))
    except ValueError:
        print("Error de formato.")
    









diasaño()
