from Filtro import Filtro

# Concrete Strategy


class Adolescentes(Filtro):

    def mostrar_peliculas(self, peliculas):
        print("Películas para adolescentes:\n")
        for pelicula in peliculas:
            if pelicula.limite_edad < 18:
                print(pelicula)
