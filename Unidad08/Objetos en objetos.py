class pelicula():

    #Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento

        print("Se creo la pelicula:", self.titulo)
        
    def __str__(self):
        return "{} lanzado en {} con duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

class catalogo:
    peliculas = []

    def __init__(self, peliculas = []):
        self.peliculas = peliculas
    
    def agregar(self, p):
        self.peliculas.append(p)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p = pelicula("El padrino", 175, 1972)
c = catalogo([p])
c.agregar(pelicula("El padrino: Parte 2", 202, 1974))

c.mostrar()