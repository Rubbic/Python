print("Hola"#Error en sitaxis

prin("Hola")#error de nombre

#Errores semanticos
lista = [1,2,3]
for i in range(4):
    if len(lista)>0:
        lista.pop()
        print(lista)
    else:
        print("la lista ya esta vacia")
"""
lista.pop()
lista.pop()
lista.pop()
print(lista)

lista.pop()
"""

#Errores de tipo de dato
n = input("Introduce un numero")

print(n + 5) #se convierte en int o float pero tambien tener cuidado si se trabajara con una cadena de datos


