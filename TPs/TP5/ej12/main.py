from Catalogo import Catalogo
from General import General
from Niños import Niños
from Adolescentes import Adolescentes
from Pelicula import Pelicula


pelicula1 = Pelicula("Pulp Fiction", 18)
pelicula2 = Pelicula("Pepa Pig", 0)
pelicula3 = Pelicula("John Wick", 13)
pelicula4 = Pelicula("El Hobbit", 7)
pelicula5 = Pelicula("9 reinas", 18)

catalogo = Catalogo(General())
catalogo.agregar_peliculas([pelicula1, pelicula2, pelicula3, pelicula4, pelicula5])

catalogo.filtrar()  # se ejecuta una estrategia. Como está asignada la estrategia General, se muestran todas las peliculas.
print("\n")
catalogo.filtro = Niños()  # se cambia la estrategia
catalogo.filtrar()  # ahora se muestran solo las peliculas para niños
print("\n")
catalogo.filtro = Adolescentes()  # se cambia la estrategia
catalogo.filtrar()  # ahora se muestran solo las peliculas para adolescentes
