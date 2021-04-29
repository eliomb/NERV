
def siguientevocal():

    # el usuario ingresa la palabra
    palabra = input("Ingresa una sentencia: ")
    
    # convierto a la lista de vocales en una lista
    vocales = "a e i o u A E I O U".split()

    # creo un diccionario usando zip()
    tupla = dict(zip(vocales, vocales[1:] + [vocales[0]])) 

    # creo una comprension de listas para hacer el reemplazo de vocales en la palabra.
    reemplazo = "".join([tupla.get(ele, ele) for ele in palabra]) 
    print("Tu palabra reemplazada: {}".format(reemplazo))

    
siguientevocal()
