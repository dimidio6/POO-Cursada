from EstadoCaja import EstadoCaja

# Concrete State


class Abierta(EstadoCaja):

    def atender(self, cliente):
        print(f"Próximo cliente: {cliente}")

    def __str__(self):
        return "Abierta"
