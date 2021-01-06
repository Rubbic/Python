a = float(input("Ingresa el primer número a sumar"))
b = float(input("Ingresa el segundo número a sumar"))

suma = a+b
resta = a-b
div = a/b 
mult = a*b
mod = a%b 
exp = a**b

print(suma)
print(resta)
print(div)
print(mult)
print(mod)
print(exp)

a = float(input("Ingresa el precio del producto"))
b = 0.18

a += (a*b)

print("El precio final de venta es: ",a)

d = float(input("Que número quieres elevar"))
n = float(input("Ingresa la potencia a utilizar"))

d**= n


print("El resultado de la potencia es ",d)


d = float(input("Ingresa el valor de a:"))
n = float(input("Ingresa el valor de n:"))

r = d**(n-1)


print("La radiación total es:",r)