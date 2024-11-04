class Torta:
    def __init__(self):
        self.__masa = str
        self.__relleno = str

    def __str__(self):
        return f"Masa: {self.masa}, Relleno: {self.relleno}"
