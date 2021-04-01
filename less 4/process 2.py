import os
import time
from multiprocessing import Process, Queue  # класс процессор и класс очередь

workers_number = 4  # специальна константа которая не будет меняться
final_fib_number = 40


def worker(tasks: Queue, answers: Queue, process_index: int):  # вычисляем числа Фибоначи process_index - айди процесса
    def fib(n: int) -> int:
        return fib(n - 1) + fib(n - 2) if n > 2 else 1

    while not tasks.empty():  # пока очередь не пуста выполняем одну очередную задачу
        number = tasks.get()
        answer = fib(number)
        answers.put((process_index, os.getpid(), number, answer,))  # чтобы посмотреть на процессы id
        # print(f"worker {process_index}, PID = {os.getpid()}: fib({number}) = {answer}")


def main():
    tasks = Queue()  # создаем очередь для заданий
    answers = Queue()  # создаем очередь для ответов
    for n in range(0, final_fib_number + 1):
        tasks.put(n)

    workers = []  # процессы
    for process_index in range(workers_number):  # в качестве парамметров функции передаем очереди
        worker_process = Process(target=worker, args=(tasks, answers, process_index,))
        workers.append(worker_process)
        print("prepared workers processes")

    start_time = time.perf_counter()
    for worker_process in workers:
        worker_process.start()
    print("started workers processes")

    for worker_process in workers:
        worker_process.join()
    # тут мы выходим из режима многозадачности. Рабоает один родительсякий процесс
    finish_time = time.perf_counter()
    print("all", finish_time - start_time)

    # Отладочная распечатка результатов
    ordered_answers = []
    while not answers.empty():
        process_index, PID, number, answer = answers.get() # PID -айди процесса
        ordered_answers.append((number, answer,))
        print(f" worker {process_index}, PID = {PID}: fib({number}) = {answer}")

    # красивая распечатка полученных результатов
    ordered_answers.sort()
    print(*(answer for number, answer in ordered_answers))



if __name__ == '__main__':
    main()
