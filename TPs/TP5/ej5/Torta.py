class Torta:
    def __init__(self):
        self.__masa = str
        self.__relleno = str

    @property
    def masa(self):
        return self.__masa

    @masa.setter
    def masa(self, masa):
        self.__masa = masa

    @property
    def relleno(self):
        return self.__relleno

    @relleno.setter
    def relleno(self, relleno):
        self.__relleno = relleno

    def __str__(self):
        return f"Masa: {self.__masa}, Relleno: {self.__relleno}"
