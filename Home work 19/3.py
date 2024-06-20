"""Определите класс Person. При создании объекта p = Person(‘Иванов’,
‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
При печати объекта должно выводиться следующее:
print(p) # чивородеФлиахиМвонавИ"""


class Person:
    def __init__(self, f, n, s):
        self.f = f
        self.n = n
        self.s = s

    def __str__(self):
        return ''.join([self.f, self.n, self.s])[::-1]


p = Person('Иванов', 'Михаил', 'Федорович')
print(p)
