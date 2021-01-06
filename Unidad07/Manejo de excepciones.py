try:
   resultado = 10/0
except ZeroDivisionError:
    print("La division entre 0 no esta definida, ingresa un numero distinto a 0")

lista=[1, 2, 3, 4, 5]
try:
    
    lista[10]
except IndexError:
    print("Estas buscando un elemento en fuera del rango de la lista\
    solo tienes 5 elementos recuerda que la numeracion comienza de 0")

colores = {'rojo':'red','verde':'green','negro':'black'}
try:
    colores['blanco']
except KeyError:
    print("La clave no esta relacionada con ningun elemento del diccionario,\n Agrega la key necesaria y su valor")
try:
    result = 15+"20"
except TypeError:
    print("Estas ingresando un dato que no es numerico, recuerda lo siguiente:\
    \n1.- Maneja numeros solamente\
    \n2.-No se aceptan cadenas ni caracteres especiales")
