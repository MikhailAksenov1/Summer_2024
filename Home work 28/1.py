"""Дан список чисел a. Назовем пару (а[i], a[j]) инверсией, если i < j, а
а[i] > a[j]. Напишите функцию, которая возвращает количество
инверсий в списке.
Например:
[1,2,3,4,5] -> 0
[5,4,3,2,1] -> 10"""

a = [5, 4, 3, 2, 1]
#a = [1, 2, 3, 4, 5]


def invers(a):
    count = 0
    for i in range(len(a)):
        for j in range(1, len(a)):
            if i < j and a[i] > a[j]:
                count += 1
    return count


print(invers(a))
