while True:
    try:
        n = float(input("Introduce un numero\t"))
        #break   #Evitar el ciclo infinito de iteraciones
    except:
        print("Ocurrio un error introduce bien el numero")
    else:
        print("Todo funciona correctamente")
        break #Puedes anidar condicionales
    finally:
        print("Fin de la iteracion")