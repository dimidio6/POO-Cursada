from BuilderTorta import BuilderTorta
from Torta import Torta


class ConcreteBuilderVainilla(BuilderTorta):
    def __init__(self):
        self.torta = Torta()

    def set_masa(self):
        self.torta.masa = "Azucarada"

    def set_relleno(self):
        self.torta.relleno = "Vainilla"
