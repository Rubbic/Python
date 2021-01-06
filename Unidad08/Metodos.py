class Galletas:
    chocolate = False
    sabor = None
    color = None
    forma = "Cuadrado"

    def __init__(self, sabor = None, color = None):#
        self.sabor = sabor
        self.color = color

        if sabor is not None and color is not None:
            print("Se creo una galleta con sabor {} de color {}".format(sabor, color))
        

    def chocolatear(self):#Siempre debe llevar self en los metodos para darle un parametro al objecto
        self.chocolate = True #Dentro del método diferenciamos los atributos del objeto antecediendo el identificador self

    def tiene_chocolate(self):
        if (self.chocolate):
            print ("Tiene chocolate")
        else:
            print("No tiene chocolate")


g = Galletas("salado", "naranja")
g.chocolatear() #Siempre debe llevar self en los metodos pero no en esta parte
g.tiene_chocolate()

print(g.chocolate)

"""
El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.

Básicamente el método __init__ remplaza al método inicializar que habíamos hecho en el concepto anterior.

Las ventajas de implementar el método __init__ en lugar del método inicializar son:

El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.
Quien utiliza POO en Python (Programación Orientada a Objetos) conoce el objetivo de este método.
Otras características del método __init__ son:

Se ejecuta inmediatamente luego de crear un objeto.
El método __init__ no puede retornar dato.
el método __init__ puede recibir parámetros que se utilizan normalmente para inicializar atributos.
El método __init__ es un método opcional, de todos modos es muy común declararlo.
"""
class Empleado:
    def __init__(self):
        self.nombre = input("Nombre del empleado:  ")
        self.sueldo = float(input("Sueldo  "))

    def mostrar(self):
        print("Nombre:  ", self.nombre)
        print("Sueldo:  ",self.sueldo)
    
    def impuesto(self):
        if self.sueldo > 3000:
            print("Pagara impuestos")
        else:
            print("No pagara impuestos")
emmpleado1=Empleado()
emmpleado1.mostrar()
emmpleado1.impuesto()

