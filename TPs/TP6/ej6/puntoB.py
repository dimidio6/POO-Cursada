from multiprocessing import parent_process, current_process, Process


def task():
    current = current_process()
    parent = parent_process()
    print(f"[{current.name}] esperando a [{parent.name}]...", flush=True)
    parent.join()  # genera un Deadlock (espera al main que no termina)


if __name__ == "__main__":
    current = current_process()
    child = Process(target=task)
    child.start()
    print(f"[{current.name}] esperando a [{child.name}]...", flush=True)
    child.join()

# Acá el Deadlock (y por ende un bucle infinito) se produce porque
# dentro de task (que sería lo que ejecuta child) se espera a parent
# y parent de child seria el proceso principal, que no puede finalizar
# ya que en él se está ejecutando el child
