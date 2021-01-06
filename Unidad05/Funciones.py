def saludar():
    c = 0
    while c < 5:
        print ("Hola esto es una funcion")
        c+=1
    
def test():
    global n
    n = 10
    print(n)

saludar()
test()

def ejemplo():
    return [23, 3, 4, 5, 5] #Retornar valores desde una funcion

print(ejemplo()[0])

def ejemplo2():
    return "Una cadena", 20, [23, 3, 4, 5, 5]

print(ejemplo2())

def suma(a, b):
    r= a + b
    return r

s = suma(4,8)
print(s)


