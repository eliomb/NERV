def numeros():
	"""esta funcion lo que debe hacer es pedir dos numeros, y usarlos para elegir dos productos"""
	numero1 = int(input("Ingrese '1' para el producto 1:"))
	numero2 = int(input("Ingrese '2' para el producto 2:"))
	if int(numero1) == 1:
		print("1: Leche condensada")
	else:
		print("Este producto no existe.")
	if int(numero2) == 2:
		print("2: Black Library Horus Heresy: Burning of Prospero")
	else:
		print("Este producto no existe.")
		
numeros()
