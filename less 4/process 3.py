import time
from multiprocessing import Pool

workers_number = 4 # количество процессов
final_fib_number = 40


def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


def main():
    tasks = list(range(0, final_fib_number))
    strt_time = time.perf_counter()
    # уход в паралельные вычисления
    with Pool(workers_number) as pool_of_processes:
        answers = list(pool_of_processes.map(fib, tasks))
    # выходим из режима многозадачности. Работает один родительский процесс
    finish_time = time.perf_counter()
    print("Время затрат:", finish_time - strt_time)

    print(*answers)


if __name__ == '__main__':
    main()
