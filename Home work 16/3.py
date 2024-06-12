"""Создайте декоратор, который переводит результат функций в
нижний регистр."""


def low(func):
    def wrapper():
        text = func()
        return text.lower()

    return wrapper


@low
def low1():
    x = input()
    return x


print(low1())
