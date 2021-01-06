class persona():
    def inicializar(self, nombre, edad):#TIenes que agregar los atributos siempre
        self.nombre=nombre
        self.edad=edad
    
    def mostrar(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)
        if self.edad >= 18:
            print(self.nombre,"es mayor de edad, con una edad de:",self.edad, "años")
        else:
            print(self.nombre,"es menor de edad, con una edad de:",self.edad, "años")
persona1=persona()
persona1.inicializar("Daphne", 26)
persona1.mostrar()

class triangulo():
    def inicializar(self):
        self.a=int(input("Ingresa uno de los lados del triangulo:  "))
        self.b=int(input("Ingresa uno de los lados del triangulo:  "))
        self.c=int(input("Ingresa uno de los lados del triangulo:  "))

    def hipotenusa(self):
        print("Lado 1:",self.a)
        print("Lado 2:",self.b)
        print("Lado 3:",self.c)
        if self.a > self.b and self.a > self.c:
            print("Este es el lado mayor:",self.a)
        else:
            if self.b > self.c:
                print("Este es el lado mayor:",self.b)
            elif self.a==self.b and self.b== self.c:
                print("Todos los lados son iguales:")
            else:
                print("Este es el lado mayor:",self.c)
    
    def clase(self):
        if self.a == self.b and self.b == self.c:
            print("Es equilatero")
        elif self.a == self.b and self.b != self.c:
            print("Es isoceles")
        else:
            print("Es escaleno")
triangulo1=triangulo()
triangulo1.inicializar()
triangulo1.hipotenusa()
triangulo1.clase()
        
#__init__

class cuadrado:
    def __init__(self):
        self.lado = int(input("Medida de los lados del cuadrado  "))
    
    def mostrar(self):
        print("Lado:  ",self.lado)
        print("Perimetro:  ",self.lado*self.lado)
        print("Area:  ",self.lado*self.lado)

cuadrado1=cuadrado()
cuadrado1.mostrar()

class operaciones:
    def __init__(self):
        self.first = float(input("Ingresa el primer número a operar  "))
        self.second = float(input("Ingresa el segundo número a operar  "))
    
    def suma(self):
        a = self.first + self.second
        print(a)

    def resta(self):
        x = int(input("Selecciona una opcion\n 1.-Primer  numero menos segundo numero  \n 2.-Segundo numero menos primer numero  "))
        if x == 1:
            b = self.first - self.second
            print(b)
        else:
            c= self.second - self.first
            print(c)

    def multiply(self):
        print("El resultado de la multiplicacion es:  ", self.first * self.second)

    def div(self):
        y = int(input("Selecciona una opcion\n 1.-Primer  numero entre segundo numero  \n 2.-Segundo numero entre primer numero  "))
        try:
            if self.first > 0 or self.second >0:
                if y == 1:
                    print("El resultado de la division es:  ", self.first/self.second)
                else:
                    print("El resultado de la division es:  ", self.second/self.first)
        except ZeroDivisionError:
            print("No esta definida la division entre 0") 

calc=operaciones()
calc.suma()
calc.resta()
calc.div()
calc.multiply()
