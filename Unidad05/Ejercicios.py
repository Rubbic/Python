"""def area(b, h):
    global a 
    a = b*h
    return a

b = int(input("Igresa la medida de la base de un rectangulo\t"))
h = int(input("Ingresa la medida de la altura del rectangulo\t"))

area(b,h)
print(a)"""

"""
def relacion(c,d):
    if c < d:
        print(-1)
    elif c == d:
        print(0)
    else:
        print(1)

c = int(input("Ingresa el primer numero a comparar\t"))
d = int(input("Ingres el segundo numero a comparar\t5"))

relacion(c,d)"""

def promedio(a,b):
    global c
    c = (a+b)/2
    return c

a = int(input("Ingresa uno de los numeros a promediar\t"))
b = int(input("Ingresa uno de los numeros a promediar\t"))

promedio(a,b)
print(c)

