import os
import time
from multiprocessing import Process, Queue  # класс процессор и класс очередь

final_fib_number = 40


def worker(task: int, process_index: int):  #  вычисляем числа Фибоначи process_index - айди процесса
    def fib(n: int) -> int:
        return fib(n - 1) + fib(n - 2) if n > 2 else 1

    number = task
    answer = fib(number)
    print(f"worker {process_index}, PID = {os.getpid()}: fib({number}) = {answer}")


def main():
    tasks = []
    for n in range(0, final_fib_number + 1):
        tasks.append(n)

    workers = []
    for process_index in range(final_fib_number + 1 ):
        worker_process = Process(target=worker, args=(tasks[process_index], process_index,))
        workers.append(worker_process)
        print("prepared workers processes")

    start_time = time.perf_counter()
    for worker_process in workers:
        worker_process.start()
    print("started workers processes")

    for worker_process in workers:
        worker_process.join()
    finish_time = time.perf_counter()
    print("all", finish_time - start_time)


if __name__ == '__main__':
    main()
