import threading
import time


def imprimir(hilo):
    for i in range(0, hilo):
        print(f"Hilo {hilo}: hola mundo")
        time.sleep(hilo)


hilo1 = threading.Thread(target=imprimir(1))
hilo2 = threading.Thread(target=imprimir(2))
hilo3 = threading.Thread(target=imprimir(3))
hilo4 = threading.Thread(target=imprimir(4))
hilo5 = threading.Thread(target=imprimir(5))
hilo6 = threading.Thread(target=imprimir(6))
