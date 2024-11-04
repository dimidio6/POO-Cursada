from Composite import Carpeta
from Leaf import Archivo

carpeta1 = Carpeta("Carpeta 1")
carpeta2 = Carpeta("Carpeta 2")

archivo1 = Archivo("Archivo 1")
archivo2 = Archivo("Archivo 2")
archivo3 = Archivo("Archivo 3")

carpeta3 = Carpeta("Carpeta 3")

archivo4 = Archivo("Archivo 4")


carpeta1.add(carpeta2)
carpeta1.add(archivo3)
carpeta2.add(archivo1)
carpeta2.add(archivo2)
carpeta3.add(archivo4)

carpeta1.mostrar()
carpeta3.mostrar()
