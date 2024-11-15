from threading import Thread

variable = 0


class Incremento(Thread):

    def run(self):
        global variable
        for i in range(5000):
            variable += 1
        print(self.name + " termina ejecución, variable: " + str(variable))


hilos = []
for i in range(4):
    hilo = Incremento()
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()
print("termina ejecución de programa")
