#Definicion del diccionario
datos = {"azul":'blue', 1:'Uno', 2:'Dos'}

print(datos)

print(datos["azul"])

#agregar datos

datos['verde'] = "green"

print(datos)

#eliminar datos

del(datos["azul"])
print(datos)

#Mostrarlo como lista

for d in datos:
    print(d)

#mostrar clave
for i in datos:
    print(datos[i])
    
#mostrar clave y valor
for c,v in datos.items():
    print(c,"-",v)

#lista de diccionarios
personajes = []

Gandalf = {"Nombre":"Gandalf","Clase":"Mago","Rasa":"Humano"}
Legolas = {"Nombre":"Legolas","Clase":"Arquero","Rasa":"Elfo"}
Gimli = {"Nombre":"Gimli","Clase":"Guerrero","Rasa":"Enano"}

personajes.append(Gandalf)
personajes.append(Legolas)
personajes.append(Gimli)

print(personajes)

for p in personajes:
    print(p["Nombre"],p["Clase"],p["Rasa"])