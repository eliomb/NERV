def factorial():
    """esta funcion de numero factorial funciona con un loop for que llega hasta donde uno indique el usuario, es decir, que si pongo '5' en el input, el for nada mas llegara hasta el 5. esto nos sirve mucho por que de esta forma podemos hacer un for con codigo que nos haga el proceso por nosotros."""
    n = int(input("Ingrese un valor: "))
    f = 1
    """lo que el calculo en el for hace es: la f se establece con el valor de '1', y en el for obtiene el valor inicial de i, y se multiplica con i subsequentemente, quedando con el valor de 1. luego, i es igual a 2 y f es igual a 1, por lo tanto f = 2, y asi hasta que se llegue a 'n'."""
    for i in range(1, n + 1):
        f = i * f
    print(f)
    
factorial()
