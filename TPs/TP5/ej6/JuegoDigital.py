from Juego import Juego


# ConcreteProductJuegoDigital
class JuegoDigital(Juego):
    def __init__(self, id, importe):
        super().__init__(id, importe)
        self.__precioPlataforma = 15.0

    def getPrecio(self):
        return self._importe * self.__precioPlataforma
