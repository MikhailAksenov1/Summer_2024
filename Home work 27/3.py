"""Дан список.
Посчитайте сколько в нем элементов, включая вложенные списки.
Например:
[] --> 0
[1, 2, 3] --> 3
["x", "y", ["z"]] --> 4
[1, 2, [3, 4, [5]]] --> 7"""

s = [1, 2, [], ["x", "y", ["z"]], [3, 4, [5, []]]]


def quantity(x):
    count = 0
    for i in x:
        count += 1

        if type(i) == list:
            count += quantity(i)

    return count


print(quantity(s))
