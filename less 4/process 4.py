# динамическое решение чисел Фибоначи
import time

final_number_fib = 40

fib = [0, 1] + [None] * (final_number_fib - 1)
start_time = time.perf_counter()
for i in range(2, final_number_fib + 1):
    fib[i] = fib[i - 1] + fib[i - 2]
for i in range(0, final_number_fib + 1):
    print(fib[i])
final_time = time.perf_counter()
print(final_time - start_time)
