# Observable


class SistemaMeteorologico:
    def __init__(self, clima):
        self._observadores = []
        self._estado_clima: str = clima

    # suscribirse
    def agregar(self, observador):
        self._observadores.append(observador)

    # desuscribirse
    def eliminar(self, observador):
        self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.actualizar(self._estado_clima)

    def modificar_clima(self, nuevo_clima):
        self._estado_clima = nuevo_clima
        self.notificar()
