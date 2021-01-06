class retangulo:
    #Constructor de la clase
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        a = self.base * self.altura
        return a

    def perimetro(self):
        p = (2*self.altura) + (2*self.base)
        