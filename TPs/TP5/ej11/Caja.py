# Context


class Caja:
    def __init__(self, cajero, estado):
        self.__cajero = cajero
        self.__estado = estado

    def cambiar_estado(self, estado):
        self.__estado = estado
        print(f"Estado de la caja cambiado a {self.__estado}")

    def atender(self, cliente):
        self.__estado.atender(cliente)
