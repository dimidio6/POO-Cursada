from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderChocolate(BuilderTorta):
    def __init__(self):
        self.__torta = Torta()

    def set_masa(self):
        self.__torta.masa = "Hojaldre"

    def set_relleno(self):
        self.__torta.relleno = "Chocolate"

    @property
    def torta(self):
        return self.__torta
