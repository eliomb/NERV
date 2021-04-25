from time import sleep

def contraseña1():
    contraseña = "hola1234"
    ingreso = input("Contraseña: ")
    intentos = 4
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Le quedan {} intentos: ".format(intentos))
        intentos -= 1
        if intentos == 3:
            if contraseña == ingreso:
                break
            print("Espere 5 segundos antes del siguiente intento.")
            sleep(5)
        elif intentos == 2:
            if contraseña == ingreso:
                break
            print("Espere 15 segundos antes del siguiente intento.")
            sleep(15)
        elif intentos == 1:
            if contraseña == ingreso:
                break
            print("Espere 45 segundos antes del siguiente intento.")
            sleep(45)
        if intentos == 0:
            print("No puede volver a intentar.")
            break

    if contraseña == ingreso:
        print("Contraseña correcta")
            
            
        

contraseña1()
