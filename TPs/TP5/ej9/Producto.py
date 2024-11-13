from abc import ABC, abstractmethod

# Component


class Producto(ABC):
    def __init__(self, precio):
        self._precio = precio

    @abstractmethod
    def getPrecio(self) -> str:
        pass
