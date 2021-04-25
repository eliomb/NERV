from time import sleep

def contraseña1():
    
    contraseña = "hola1234"
    ingreso = input("Contraseña: ")
    intentos = 4
    valida = False

    
    while ingreso != contraseña:
        ingreso = input("Contraseña incorrecta! Le quedan {} intentos: ".format(intentos))
        intentos -= 1

        
        if intentos == 3:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Espere 5 segundos antes del siguiente intento.")
            sleep(5)

            
        elif intentos == 2:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Espere 15 segundos antes del siguiente intento.")
            sleep(15)

            
        elif intentos == 1:
            if contraseña == ingreso:
                valida = True
                print("Contraseña correcta")
                return(valida)
            print("Espere 45 segundos antes del siguiente intento.")
            sleep(45)

            
        if intentos == 0:
            valida = False
            print("No puede volver a intentar.")
            return(valida)

                
    if contraseña == ingreso:
        valida = True
        print("Contraseña correcta")
        return(valida)
            

contra = contraseña1()

if contra == True:
    print("Has ingresado la contraseña correctamente.")

