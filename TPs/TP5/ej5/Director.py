from BuilderTorta import BuilderTorta


class Director:
    def __init__(self, builder: BuilderTorta):
        self._builder = builder

    def build_torta(self):
        self._builder.set_masa()
        self._builder.set_relleno()