#Definir un conjunto vacio
conjunto = {1,2,3}

conjunto.add(4)
conjunto.add(0)
conjunto.add("H")
conjunto.add("A")
conjunto.add("Z")

print(conjunto)

#Datos no se repiten en conjuntos

nombres = {"Alex","Alex","Alex"}
print("Alex" not in nombres)
print(nombres)

#Conversiones con listas

lista = {1,2,3,3,2,1}
print(lista)

conjunto = set(lista)
print(conjunto)
lista = list(conjunto)
print(lista)

#Conversiones simplificadas

lista = {1,2,3,3,2,1}
print(lista)

lista = list(set(lista))
print(lista)

#Conversion con cadenas
cadena = "Al pan pan y al vino vino"
print(set(cadena))