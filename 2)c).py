def areaejes():
    """Esta funcion utiliza cuatro variables como coordenadas, y en base a ellas, calcula la base y la altura del rectangulo dado para calcular su superficie."""
    x1 = int(input("Introduzca la primera coordenada X: "))
    x2 = int(input("Introduzca la segunda coordenada X: "))
    y1 = int(input("Introduzca la primera coordenada Y: "))
    y2 = int(input("Introduzca la segunda coordenada Y: "))
    h = y2 - y1
    b = x2 - x1
    print(h, b)
    if h > 0 and b > 0:
        area = b * h
        print("El area es: ", area)
    else:
        print("NO puede ser negativo, ni igual a CERO!")
        return
    

areaejes()

