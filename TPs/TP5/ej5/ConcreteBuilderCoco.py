from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderCoco(BuilderTorta):
    def __init__(self):
        self.__torta = Torta()

    def set_masa(self):
        self.__torta.masa = "Azucarada"

    def set_relleno(self):
        self.__torta.relleno = "Coco"

    @property
    def torta(self):
        return self.__torta
