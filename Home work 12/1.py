"""Создайте функцию, которая принимает на вход список X и
возвращает в качестве результата два списка:
Список индексов элементов равных минимальному значению
списка X
Список индексов элементов равных максимальному значению
списка X
Например:
Ввод: X = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
Вывод: [0, 4, 8], [3, 7, 9]"""

def in_min_max(x):
    mi= min(x)
    ma = max(x)
    lst_min = [i for i in range(len(x)) if x[i] == mi]
    lst_max = [i for i in range(len(x)) if x[i] == ma]
    return lst_min, lst_max
print(*in_min_max([1, 2, 3, 4, 1, 2, 3, 4, 1, 4]))
