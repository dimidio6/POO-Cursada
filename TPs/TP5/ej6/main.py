from Creator import Creator
from ConcreteCreatorJuegoFisico import ConcreteCreatorJuegoFisico
from ConcreteCreatorJuegoDigital import ConcreteCreatorJuegoDigital


def obtener_precio(creator: Creator) -> None:
    print(
        f"Cliente: Desea obtener el precio del juego, no conoce en que formato viene.\n"
        f"{creator.infoJuego()}"
    )


print("Juego físico:")
obtener_precio(ConcreteCreatorJuegoFisico())
print("")
print("Juego digital:")
obtener_precio(ConcreteCreatorJuegoDigital())
