"""Напишите функцию, которая находит оптимальный маршрут из верхнего
левого угла в правый нижний угол матрицы. Двигаться можно только вправо
или вниз. В каждой клетке матрице содержится число. Оптимальным
считается маршрут с минимальной суммой чисел клеток, через которые
проходит маршрут.
Например, если матрица 3 х 3: , то оптимальным будем маршрут,
который проходит через клетки 10 + 5 + 1 + 2 + 70 = 88.
Подсказка: полный перебор вариантов заведомо неэффективен.
Возможное решение – идти от начала и запоминать оптимальные маршруты
для каждой клетки из начала."""

matrix = [[10, 20, 30], [5, 1, 80], [90, 2, 70]]

n = len(matrix)
solutions = [[0 for i in range(n)] for j in range(n)]
solutions[0][0] = matrix[0][0]
for i in range(1, n):
    solutions[i][0] = solutions[i - 1][0] + matrix[i][0]

for j in range(1, n):
    solutions[0][j] = solutions[0][j - 1] + matrix[0][j]


def calculate_path(i, j):
    if (solutions[i][j] > 0):
        return solutions[i][j]

    top = calculate_path(i - 1, j) + matrix[i][j]
    left = calculate_path(i, j - 1) + matrix[i][j]

    if (top < left):
        solutions[i][j] = top
        return top
    else:
        solutions[i][j] = left
        return left


print(calculate_path(n - 1, n - 1))
