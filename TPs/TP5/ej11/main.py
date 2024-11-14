from Banco import Banco
from Abierta import Abierta
from Suspendida import Suspendida
from Cerrada import Cerrada
from Cliente import Cliente

cliente1 = Cliente("Bruno", 25)
cliente2 = Cliente("Dani", 55)
cliente3 = Cliente("Pepe", 65)
cliente4 = Cliente("Miguel", 75)

# Concrete State --> Abierta
banco = Banco("Juan", Abierta())
banco.caja.atender(cliente1)
# Concrete State --> Suspendida
banco.caja.cambiar_estado(Suspendida())
banco.caja.atender(cliente2)
banco.caja.atender(cliente3)
# Concrete State --> Cerrada
banco.caja.cambiar_estado(Cerrada())
banco.caja.atender(cliente4)
