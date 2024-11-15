from multiprocessing import Process, Value, Lock


variable = Value("i", 0)  # "i" = entero


class Incremento(Process):

    def run(self):
        for i in range(5000):
            with Lock():
                variable.value += 1
        print(self.name + " termina ejecución, variable: " + str(variable.value))


if __name__ == "__main__":

    hilos = []
    for i in range(4):
        hilo = Incremento()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()
        hilo.join()

    print("termina ejecución de programa")
