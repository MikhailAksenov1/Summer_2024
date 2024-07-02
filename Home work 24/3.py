"""Создайте функцию, которая принимает на входе строку из открывающих и
закрывающих круглых скобок.
Функция возвращает False, если число скобок "(" не равно числу скобок ")".
Функция возвращает True, если в любой подстроке, начинающейся с начала, число
скобок ")" не превышает число скобок ")".
Функция возвращает False во всех остальных случаях.
Примеры:
"()" => true
")(()()" => false
"(" => false
"(()) (( () () ) () )" => true
"())(()" => false"""

import re


def check(x):
    if x.count('(') != x.count(')'):
        return False
    else:
        try:
            s = re.match(r'\(.*[^(]\)|\(.*[^)]\)|\(\)', x).group(0)
            if s == x:
                return True
            else:
                return False
        except AttributeError:
            return False


x = input()
print(check(x))
