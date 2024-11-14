# Context


class Catalogo:
    def __init__(self, filtro):
        self.__peliculas = []
        self.__filtro = filtro  # estrategia

    @property
    def filtro(self):
        return self.__filtro

    @filtro.setter
    def filtro(self, filtro):
        self.__filtro = filtro

    def filtrar(self):  # ejecuta la estrategia
        self.__filtro.mostrar_peliculas(self.__peliculas)

    def agregar_peliculas(self, lista):
        for pelicula in lista:
            self.__peliculas.append(pelicula)
