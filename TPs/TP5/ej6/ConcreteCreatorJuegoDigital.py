from Creator import Creator
from Juego import Juego
from JuegoDigital import JuegoDigital


class ConcreteCreatorJuegoDigital(Creator):

    def factory_method(self) -> Juego:
        return JuegoDigital(700, 4500.00)
