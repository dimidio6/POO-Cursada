from Creator import Creator
from Juego import Juego
from JuegoFisico import JuegoFisico


class ConcreteCreatorJuegoFisico(Creator):

    def factory_method(self) -> Juego:
        return JuegoFisico(900, 5000.00)
