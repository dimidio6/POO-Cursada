from EstadoCaja import EstadoCaja

# COncrete State


class Suspendida(EstadoCaja):

    def atender(self, cliente):
        if cliente.edad > 60:
            print(f"Próximo cliente: {cliente}")
        else:
            print("Caja en espera...")

    def __str__(self):
        return "Suspendida"
