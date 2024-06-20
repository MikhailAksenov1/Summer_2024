"""Реализуйте класс Fibonacci, который реализует итератор, генерирующий
бесконечную последовательность чисел Фибоначчи.
Например:
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
Должен печатать следующие числа:
1
1
2
3"""


class Fibonacci:
    def __init__(self):
        self.first = 1
        self.second = 0

    def __iter__(self):
        return self

    def __next__(self):
        s = self.second
        self.second += self.first
        self.first = s
        return self.second


fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
