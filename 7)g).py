from calendar import monthrange
import datetime

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

fechavalida()
