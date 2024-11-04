from Component import ComponentAdministracion


class Archivo(ComponentAdministracion):

    def mostrar(self):
        print(f"File: {self._name}")
