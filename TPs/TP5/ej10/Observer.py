from abc import ABC, abstractmethod

# Suscriber


class Observer(ABC):

    @abstractmethod
    def actualizar(self, estado_clima):
        pass
