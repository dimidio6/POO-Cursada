from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderChocolate(BuilderTorta):
    def __init__(self):
        self.torta = Torta()

    def set_masa(self):
        self.torta.masa = "Hojaldre"

    def set_relleno(self):
        self.torta.relleno = "Chocolate"
