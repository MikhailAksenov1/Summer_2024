"""Напишите функцию, которой на вход подается строка, содержащая
последовательность слов (которые могут включать буквы верхнего и нижнего
регистра). На выходе должна получиться строка в CamelStyle.
Например, "cAmel CAse woRD" => CamelCaseWord"""


def Aa_Bb(x):
    x = x.split(' ')
    res = ''
    for i in x:
        res += i.capitalize()
    return res


print(Aa_Bb(input()))
