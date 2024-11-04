from abc import ABC, abstractmethod


# Component implementado cómo clase abstracta para este caso
class ComponentAdministracion(ABC):
    def __init__(self, name):
        self._name = name

    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abstractmethod
    def mostrar(self) -> str:
        pass

    def es_carpeta(self) -> bool:
        return False
