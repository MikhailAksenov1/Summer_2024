"""Создайте класс, экземпляр которого генерирует бесконечную
циклическую последовательность из чисел и больших латинский букв.
1, A, 2, B, 3, C, .., X, 25, Y, 26, Z,1,A,2,B,3,C,..,X,25,Y,26,Z, 1, A…"""


class Wh:
    def __init__(self):
        self.count = 0
        self.alphabet = 64
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if chr(self.alphabet) == 'Z':
            self.count = 0
            self.alphabet = 64
            self.counter = 0
        if self.counter % 2 == 0:
            self.count += 1
            self.counter += 1
            return self.count
        else:
            self.alphabet = (self.alphabet + 1)
            self.counter += 1

            return chr(self.alphabet)
wh = Wh()
while True:
    print(next(wh))
