# interfaz Constructora

from abc import ABC, abstractmethod


class BuilderTorta(ABC):

    @abstractmethod
    def set_masa(self):
        pass

    @abstractmethod
    def set_relleno(self):
        pass
