"""Введите число n от 1 до 18.
Напечатайте квадратную матрицу, имитирующую Дартс.
Например для n = 5.
1 1 1 1 1
1 2 2 2 1
1 2 3 2 1
1 2 2 2 1
1 1 1 1 1"""


def matrix(n):
    m = [[1 for i in range(n)] for i in range(n)]
    for i in range(1, n):
        for k in range(i, n - i):
            m[i][k] = i + 1
            m[k][i] = i + 1
            m[-i - 1][k] = i + 1
            m[k][-i - 1] = i + 1
    for i in m:
        print(i)


n = int(input())
matrix(5)
