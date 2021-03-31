# исползование генераторов
import itertools
from functools import reduce


def f(x):
    return x * 10


E = range(10000)  # армефметическая прогрессия
print(E[1000])  # выполнение действие объектом Е
A = (1, 2, 3, 4, 5)
B = (f(x) for x in A)  # он пока ничего не вычислил, пока циклом фор не прошлись по значениям
for y in B:
    print(y)


# функция map почти как генератор

# создадим функцию  которой передадим функцию в качестве парметра
def double_performer(f, x):
    return f(f(x))


print(double_performer(f, 5))

D = [1, 23, 4, 5]

C = map(f, D)
for y in C:
    print(y)

A = range(10)
# пройдемся генератором. Он не хранит в себе вычисления, а вычисляет только тогда значение когда он нужно
B = (x for x in A if x % 2 == 0)
print(*B)
print(*(x * x for x in A if x % 2 == 1))
# либо использование лямбды функции безмянной просто предаем первый аргумент параметр и потом выражение
print(*map(lambda x: x * x, A))

L = (1, 2, 3, 4, 5)
K = tuple(x * 10 for x in L)
print(K)
C = zip(L, K)
for i in C:
    print(i)

for a, b in zip(L, K):
    print(a, b, a + b)

# нумирация

for i, char in enumerate("hello"):  # i это индекс строки char обект индекса
    print(i, char)


# пример сопрограммы на генераторе
def aritm_progression(start, stop, step):
    x = start
    while x < stop:
        print(f"now working on x ={x}")
        yield x
        x += step


G = aritm_progression(1, 10, 2)
for x in G:
    print(x)

# генераторы itertools
print("генераторы itertools")
from itertools import *

H = [1, 2, 3, 4, 5]
for i in itertools.accumulate(H):
    print(i)
for i in combinations("absd", 2):
    print(i)

# перестановки
for p in permutations("ABC"):
    print(p)
    print(*p)

file = open("text.txt", "w")

l = [str(i) + str(i - 1) for i in range(20)]
for index in l:
    file.write(index + "/n")
file.close()

# функция reduce из  functools
A = (1, 2, 3, 4, 5)
B = reduce(lambda x, y: x + y, A)
print(B)
