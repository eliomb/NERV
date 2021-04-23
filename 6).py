
numeros = []
def multiplicacion():
    """esta funcion debe pedir cuatro numeros, y de entre los cuatro, multiplicar dos de ellos y ver cual es el mayor resultado de la multiplicacion de entre dos de los numeros"""
    for i in range(0, 4):
            num = int(input("Ingrese cuatro numeros: "))
            numeros.append(num)
    mayor = 0
    resultado = 0
    for i in range(0, 4):
        print(numeros[i])
        a = numeros[i]
    """aca hay un doble for. mientras i esta parado en un numero de la lista, el segundo for va a pasar por el resto de los numeros de la lista, y a dentro validamos que ambos numeros no sean los mismos a si no se multipliquen entre si."""
        for x in range(0, 4):
            resultado = abs(a * numeros[x])
            if resultado > mayor and numeros[i] != numeros[x]:
                mayor = resultado

    print("El mayor valor es: ", mayor)

"""print(list(map(multiplicacion, numeros)))"""

multiplicacion()






