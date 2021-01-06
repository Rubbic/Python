def cuenta_regresiva(n):
    n -=1
    if n > 0:
        print(n)
        cuenta_regresiva(n)
    else:
        print("BOOOM")

cuenta_regresiva(5)

def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("Valor inicial ->",num)
    return num

print(factorial(5))