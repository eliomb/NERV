def temperaturas():
    fah = float(input("Ingresa una temperatura en fahrenheit: "))
    cel = (fah - 32) * 5/9
    print("Esta es su conversion a celsius: ", cel)

temperaturas()
