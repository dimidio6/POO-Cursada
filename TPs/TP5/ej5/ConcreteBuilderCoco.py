from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderCoco(BuilderTorta):
    def __init__(self):
        self.torta = Torta()

    def set_masa(self):
        self.torta.masa = "Azucarada"

    def set_relleno(self):
        self.torta.relleno = "Coco"
