
def contraseña1():
    contraseña = "hola1234"
    ingreso = input("Contraseña: ")
    intentos = 4
    while ingreso != contraseña and intentos > 0:
        ingreso = input("Contraseña incorrecta! Le quedan {} intentos: ".format(intentos))
        intentos -= 1

    if intentos == 0:
        print("No puede volver a intentar.")
        
    if contraseña == ingreso:
        print("Contraseña correcta")

contraseña1()
