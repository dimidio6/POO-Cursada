from DecoradorProducto import DecoradorProducto

# Concrete Decorator


class ARS(DecoradorProducto):

    def getPrecio(self):
        return "$ARS " + self._producto.getPrecio()
