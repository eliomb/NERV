
def contraseña1():
    contraseña = "hola1234"
    ingreso = input("Contraseña: ")
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Le quedan {} intentos: ".format(intentos))
    
    if contraseña == ingreso:
        print("Contraseña correcta")

contraseña1()
