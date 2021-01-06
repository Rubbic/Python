opcion = 0

while opcion < 10:
    print(opcion)
    
    if opcion == 5:
        print("Detente en el numero 5")
        break

    opcion += 1
else:
    print("Termino el ciclo while")