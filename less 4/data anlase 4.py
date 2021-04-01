# время вычислений списка Фибоначи
import time

final_fib_number = 40


def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


if __name__ == '__main__':
    tasks = list(range(0, final_fib_number + 1))
    start_time = time.perf_counter()
    answer = []
    for number in tasks:
        answer.append(fib(number))
    finish_time = time.perf_counter()
    print("Затраченное время:", finish_time - start_time)
