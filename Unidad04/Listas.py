#Definicion de lista
numeros = [1,2,3,4,5]
datos = [5,"Cadena",5.5,"texto"]

print(numeros)
print(datos)

#Mostramos datos de la lista por indice
print(datos[-1])

#Mostramos datos por slicing
print(datos[0:2])
print(datos[0:3])
print(datos[:-2])

#Suma de listas
listas = numeros + datos
print(listas)

#Mutabilidad
pares = [0,2,4,5,8,10]
pares[3] = 6
print("Pares",pares)

#Append
pares.append(12)
print("Pares",pares)