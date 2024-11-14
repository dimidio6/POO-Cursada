from Filtro import Filtro

# Concrete Strategy


class Niños(Filtro):

    def mostrar_peliculas(self, peliculas):
        print("Películas para niños:\n")
        for pelicula in peliculas:
            if pelicula.limite_edad < 13:
                print(pelicula)
