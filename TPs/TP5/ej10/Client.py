from SistemaMeteorologico import SistemaMeteorologico
from Reportero import Reportero

observable = SistemaMeteorologico("despejado")
observador = Reportero()

observable.agregar(observador)  # suscribe un observador para que se lo notifique
observable.modificar_clima("nublado")  # modificar_clima notifica a los observadores
observable.modificar_clima("ventoso")
