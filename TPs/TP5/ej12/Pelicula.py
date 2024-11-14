class Pelicula:
    def __init__(self, nombre, limite_edad):
        self.__nombre = nombre
        self.__limite_edad = limite_edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def limite_edad(self):
        return self.__limite_edad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Limite de edad: {self.__limite_edad}"
