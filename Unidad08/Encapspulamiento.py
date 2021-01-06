class ejemplo:
    __atributo_privado = "Soy confidencial" #No puedes acceder cuando estan con dos __ al inicio

    def __metodo_privado(self): #__ no permite aceder
        print("Soy un metodo confindencial inalacanzable desde afuera")
    
    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = ejemplo()

# print(e.__atributo_privado)
print(e.atributo_publico())
e.metodo_publico()

# e.__metodo_privado()

"""Acceder a atributos y metodos privados, mediante metodos publicos
definidos por nosotros, algo muy parecido al ingreso por validacion"""