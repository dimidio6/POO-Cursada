from Producto import Producto

# Base Decorator


class DecoradorProducto(Producto):
    def __init__(self, producto):
        self._producto = producto  # wrappee

    def getPrecio(self):
        pass
