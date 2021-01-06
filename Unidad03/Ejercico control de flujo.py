from test.test_import.data.unwritable import x

"""
a = input("Ingresa el primer numero")
b = input("Ingresa el segundo numero")

if a > b:
    print("El numero mayor es: ",a)
elif a == b:
    print ("Los numeros %s y %s son iguales"%(a,b))
else:
    print("El numero mayor es: ", b)
"""

x = int(input("Ingresa un numero positivo, negativo o neutro"))

if x > 0:
    print("El numero %s es positivo"%x)
elif x < 0:
    print("El numero %s es negativo"%x) 
else:
    print("El numero %s es neutro"%x)
