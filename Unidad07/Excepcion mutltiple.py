try:
    n = float(input("Intoduce un numero  "))
    print(5/n)

except TypeError:
    print("No se puede dividir entre una cadena")

except ValueError:
    print("Debes introducir un numero")

except ZeroDivisionError:
    print("No es posible dividir entre 0")

except Exception as e: #Guardamos la excepcion como una variable
    print("Ha ocurrido un error =>", type(e).__name__)

