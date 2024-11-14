from Caja import Caja


# Banco que administra una Caja
# solo agrega una capa extra al enunciado, pero no es necesario para el State.


class Banco:
    def __init__(self, cajero, estado):
        self.__caja = Caja(cajero, estado)

    @property
    def caja(self):
        return self.__caja
