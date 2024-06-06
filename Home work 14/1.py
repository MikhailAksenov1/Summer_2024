"""Напишите рекурсивную функцию, которая вычисляет количество
цифр введенного целого числа n (n >= 0)."""

def quantity(n, i = 1):
    if n >= 10:
        i = quantity(n//10, i+1)
    return i
print(quantity(int(input())))

