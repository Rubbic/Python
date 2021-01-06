#Definicion de una tupla
tupla = (100,"Hola",[1,2,3],-50)

for d in tupla:
    print(d) 

"""Es inmutable
tupla[0] = 50
"""
#Funciones de tuplas
print(len(tupla[2]))

print(tupla.index(100))

print(tupla.count(100))