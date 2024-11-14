from abc import ABC, abstractmethod

# State


class EstadoCaja(ABC):

    @abstractmethod
    def atender(self, cliente):
        pass
