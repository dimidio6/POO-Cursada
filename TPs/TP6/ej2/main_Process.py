from multiprocessing import Process, Value, Lock


variable = Value("i", 0)  # "i" = entero


class Incremento(Process):

    def run(self):
        for i in range(5000):
            with Lock():
                variable.value += 1
        print(self.name + " termina ejecución, variable: " + str(variable.value))


if __name__ == "__main__":

    procesos = []
    for i in range(4):
        proceso = Incremento()
        procesos.append(proceso)

    for proceso in procesos:
        proceso.start()
        proceso.join()

    print("termina ejecución de programa")
