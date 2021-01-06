v = "otro texto"
n=10

c= "Un texto '{}' y un número '{}'".format(v,n) #identificadores referenciados
print(c)

"""Se pueden modificar el orden de las variables y estas se mostraran de esa manera"""

print("{:>30}".format("palabra")) #Alineamiento de n cantidad de caracteres Derecha
print("{:30}".format("palabra")) #Alineamiento de n cantidad de caracteres Izquierda
print("{:^30}".format("palabra")) #Alineamiento de n cantidad de caracteres Centro

print("{:.3}".format("palabra")) #truncamiento a tres caracteres
print("{:>30.3}".format("palabra")) #truncamiento a tres caracteres y a la derecha

print("{:04d}".format(10)) 
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

nombre = "Alex"
texto = "Hola  {}".format(nombre)
print(texto)

texto = f"Hola {nombre}" #La nueva version reduce format a esta sintaxis
print(texto)