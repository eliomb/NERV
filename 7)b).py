from calendar import monthrange
import datetime
def mes():
    """lo que esta funcion hace es utilizar las librerias de calendario y datetime, de la cual utilizo sus funciones y statements para poder sacar el nombre de mes y la cantidad de dias en un mes, y este numero de dias cambia dependiendo en si es un año bisiesto."""
    year = int(input("ingrese el año: "))
    month = int(input("Ingrese el numero de mes: "))
    if month > 12 or year > 10000:
        print("Ingrese un mes valido o un año razonable.")
    else:
        day = monthrange(year, month)[1]
        monthobj = datetime.datetime.strptime(str(month), "%m")
        monthname = monthobj.strftime("%b")
        print(day)
        print("La cantidad de dias en el mes {} del año {} es de: {}".format(monthname, year, day))
mes()
