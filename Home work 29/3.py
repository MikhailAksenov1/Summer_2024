"""Напишите функцию, которая проверяет, являются ли два слова изоморфными.
Два слова изоморфны, если буквам одного слова можно сопоставить (map)
буквам другого слова.
True:
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
False:
AB CC
XXY XYY
ABAB CD"""

def izomorf(a, b):
    c = {}
    if len(a) != len(b):
        return False
    else:
        for i, j in  zip(a, b):
            if i not in c and j not in c.values():
                c[i] = j
            elif i in c and c[i] == j:
                continue
            else:
                return False
    return True
print(izomorf(a=input(), b=input()))

