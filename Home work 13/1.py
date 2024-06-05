"""Создайте функцию-генератор, которая создает бесконечную
последовательность:
1, -2, 3, -4, 5, -6, …"""


def fu():
    c = 1
    while True:
        if c % 2==0: yield -c
        else: yield c
        c += 1


gf = fu()
for _ in range(int(input())):
    print(next(gf), end=',')



