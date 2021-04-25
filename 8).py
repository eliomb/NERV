listanumeros = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def romanos():
    """
    esta funcion anda gracias a una list que contiene la tabla de conversion entre numeros
    decimales a numeros romanos. lo que la funcion hace es que utiliza un for con dos variables
    que recorren a ambos valores de la lista, y dentro del for hay un while que agrega los valores
    correspondientes en romano solo cuando nuestra variable "numero" es mayor o igual a su correspondiente "i".
    luego, se le resta "i" a "numero" y se sigue disecando el numero hasta que se consigan todos los
    valores en romano.
    """
    romano = ""
    numero = int(input("Ingrese un año: "))
    num = numero
    if numero > 0 and numero < 10000:
        for i, x in listanumeros:
            while numero >= i:
                romano = romano + x
                numero = numero - i
        print("El año {} es {} en numerales romanos.".format(num, romano))
    else:
        print("Ingrese un año razonable.")




romanos()



