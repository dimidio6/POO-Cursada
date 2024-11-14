from abc import ABC, abstractmethod

# Strategy (interfaz)


class Filtro(ABC):

    @abstractmethod
    def mostrar_peliculas(self, peliculas):
        pass
