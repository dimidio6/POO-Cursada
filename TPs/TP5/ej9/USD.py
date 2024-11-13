from DecoradorProducto import DecoradorProducto

# Concrete Decorator


class USD(DecoradorProducto):

    def getPrecio(self):
        return "$USD " + self._producto.getPrecio()
