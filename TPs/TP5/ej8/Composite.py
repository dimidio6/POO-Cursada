from Component import ComponentAdministracion


class Carpeta(ComponentAdministracion):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def mostrar(self):
        print(f"Carpeta: {self._name}")
        for archivo in self._children:
            archivo.mostrar()

    def es_carpeta(self):
        return True
