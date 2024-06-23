"""Напишите функцию, которая на вход получает DataFrame, который
содержит числа и строки, а в качестве результата возвращает
сумму всех чисел."""

import pandas as pd

sp = [12, 'abc', 10, 'cde', '10', 57, 1, '20', 1, 40, 'gtr']


def sum(df):
    su = 0
    for i in df.index:
        for j in df.columns:
            x = df.loc[i, j]
            if type(x) == int:
                su += x

    return su


df1 = pd.DataFrame([12, 'abc', 10, 'cde', '10', 57, 1, '20', 1, 40, 'gtr'])

print(sum(df1))
