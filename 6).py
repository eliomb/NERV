def multiplicacion(numero):
    return numero * (numero + 1)
        
    
numeros = []

for i in range(0, 4):
        num = int(input("Ingrese cuatro numeros: "))
        numeros.append(num)


print(list(map(multiplicacion, numeros)))




