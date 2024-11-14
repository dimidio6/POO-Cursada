from EstadoCaja import EstadoCaja

# Concrete State


class Cerrada(EstadoCaja):

    def atender(self, cliente):
        print("La caja esta cerrada, no se puede atender.")

    def __str__(self):
        return "Cerrada"
