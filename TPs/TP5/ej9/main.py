from ProductoConcreto import ProductoConcreto
from ARS import ARS
from USD import USD

producto = ProductoConcreto(90000.500)
producto_ars = ARS(producto)
producto_usd = USD(producto)

print(producto.getPrecio())
print(producto_ars.getPrecio())
print(producto_usd.getPrecio())
