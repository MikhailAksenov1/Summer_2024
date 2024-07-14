"""Дан список, который состоит из одинаковых чисел за исключением одного.
Найдите это число."""

sp = [10, 10, 10, 10, 10, 2]
for i in range(len(sp)):
    if i + 1 != len(sp):
        if sp[i] != sp[i + 1] and sp[i] != sp[i - 1]:
            print(sp[i])
            break
    else:
        if sp[i] != sp[i - 1]:
            print(sp[i])
