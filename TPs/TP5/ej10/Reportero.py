from Observer import Observer

# ConcreteSuscribe (Observador concreto)


class Reportero(Observer):

    def actualizar(self, estado_clima):
        print(f"Reportero: El clima cambió a {estado_clima}")
