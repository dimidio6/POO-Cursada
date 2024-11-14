from Filtro import Filtro

# Concrete Strategy


class General(Filtro):

    def mostrar_peliculas(self, peliculas):
        print("Películas para todos:\n")
        for pelicula in peliculas:
            print(pelicula)
