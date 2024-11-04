from abc import ABC, abstractmethod


# Product (clase abstracta para este caso)
class Juego(ABC):
    def __init__(self, id, importe):
        self._id = id
        self._importe = importe

    @abstractmethod
    def getPrecio(self):
        pass
