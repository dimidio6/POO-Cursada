class Cliente:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"


# no es necesaria para el State.
