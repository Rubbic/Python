class pelicula():

    #Constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
    
    #Destructor de la clase
    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)
    
    def __str__(self):
        return "{} lanzado en {} con duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    def __len__(self):
        return self.duracion
         
p =  pelicula("El Padrino",175,1973)
# del(p)


print(str(p))
print(len(p))