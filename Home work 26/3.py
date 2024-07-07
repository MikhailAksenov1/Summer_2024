"""Создайте метод Person, определите в нем атрибут self._age
Используйте декоратор @property для определения методов getter,
setter, deleter.
В методе setter определите проверку, что возраст не может быть
меньше 1 и больше 100, при попытке установить этот возраст
программа должна печатать «Недопустимый возраст»."""


class Person():
    def __init__(self, _age):
        self._age = _age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 1 <= age <= 100:
            self._age = age
        else:
            print('Недопустимый возраст')

    @age.deleter
    def age(self):
        del self._age




Tom = Person(24)
print(Tom.age)
Tom.age = 22
print(Tom.age)
del Tom.age
print(Tom.age)


