from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def infoJuego(self) -> str:
        juego = self.factory_method()
        result = f"Precio: {juego.getPrecio()}"

        return result
