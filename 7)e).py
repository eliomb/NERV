from calendar import monthrange
import datetime

"""
usando nuevamente mi funcion anterior para regresar una fecha con un formato valido, hago una funcion que
primero mide la cantidad de dias en un año dado, asi sea bisiesto o no, y usando un for lo consigo, guardando
el numero total de dias en una variable.
en otro for, recorro el año unicamente hasta cuando i sea igual al numero de mes que el usuario metio, y hasta alli
se consiguen los dias hasta el mes elegido, pero luego esta la cantidad de dias, las cuales les resto al valor total del
mes elegido y este valor que consigo se lo resto a la variable que contiene los dias hasta el mes actual. exactamente
despues de esto, hago un try except que haga la cuenta necesaria para calcular la fecha actual.
"""
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



def diasaño():
    diastotal = 0
    diashastafecha = 0
    diasrestantes = 0
    date = fechavalida()
    formato = "%d/%m/%Y"
    fechaobjeto = datetime.datetime.strptime(date, formato)
    año = fechaobjeto.year
    mes = fechaobjeto.month
    dia = fechaobjeto.day
    tr = monthrange(año,mes)[1]
    diames = tr - dia
    """
    perdon por el choclo de variables :)
    """
    
    for i in range(1,13):
        dias = monthrange(año, i)[1]
        diastotal = diastotal + dias
    for i in range(1,13):
        if i <= mes:
            dias2 = monthrange(año, i)[1]
            diashastafecha = diashastafecha + dias2
    try:
        diasrestantes = diastotal - (diashastafecha - diames)
        print("Quedan {} dias para que finalice el año {}.".format(diasrestantes, año))
    except ValueError:
        print("Error de formateo.")
diasaño()
