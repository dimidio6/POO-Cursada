from Producto import Producto

# ConcreteComponent


class ProductoConcreto(Producto):

    def getPrecio(self):
        precio_str = f"{self._precio:.2f}"
        return precio_str
