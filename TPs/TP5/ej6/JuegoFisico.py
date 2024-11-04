from Juego import Juego


# ConcreteProductJuegoFisico
class JuegoFisico(Juego):
    def __init__(self, id, importe):
        super().__init__(id, importe)
        self.__precioTraslado = 20.0

    def getPrecio(self):
        return self._importe * self.__precioTraslado
