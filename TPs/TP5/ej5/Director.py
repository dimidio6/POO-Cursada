from BuilderTorta import BuilderTorta


class Director:
    def __init__(self):
        self._builder = None

    def build_torta(self):
        self._builder.set_masa()
        self._builder.set_relleno()

    @property  # setea un builder en el director
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderTorta):
        self._builder = builder
