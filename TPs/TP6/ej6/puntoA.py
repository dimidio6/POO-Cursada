from multiprocessing import Process
from multiprocessing import Lock


def task(Lock):
    print("Adquiriendo el lock...", flush=True)
    with Lock:
        print("Adquiriendo el lock otra vez...", flush=True)
    with Lock:  # acá se generaba el Deadlock
        pass


if __name__ == "__main__":
    lock = Lock()
    process = Process(target=task, args=(lock,))
    process.start()
    process.join()
