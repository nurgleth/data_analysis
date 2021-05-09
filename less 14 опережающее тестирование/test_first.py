import unittest


def fib(n):
    """
    Вычисляет число Фибонаачи номер n.
    Выбрасывает исколючение TypeError, если вызвана не для целочисленного типа.
    Выбрасывает исколючение ValueError, если число отрицательное или больше допустимого
    :param n: цело число от 0 до 9999
    :return: цело число от 0 до ...
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with class <int>")
    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers")
    if n >= 10000:
        raise ValueError("Fibonacci can't work with numbers larger than 9999")
    if not n:
        return 0
    f_2 = 0
    f_1 = 1
    for i in range(2, n + 1):
        f_1, f_2 = f_1 + f_2, f_1
    return f_1


class TestFibonacci(unittest.TestCase):

    def test_simple(self):
        for param, result in [(0, 0), (1, 1), (3, 2), (10, 55)]:
            self.assertEqual(fib(param), result)

    def test_stress(self):
        self.assertEqual(fib(9999), fib(9998) + fib(9997))
        with self.assertRaises(ValueError):
            fib(10000)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)

    def test_wrong_param_type(self):
        with self.assertRaises(TypeError):
            fib("Hello")
        with self.assertRaises(TypeError):
            fib(2.5)


class TestStringMethods(unittest.TestCase):  # тест строки

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')  # сравнение

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())  # проверка на провдивость
        self.assertFalse('Foo'.isupper())  # проверка на провдивость

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):  # проверка типа
            s.split(2)


if __name__ == '__main__':
    unittest.main()
