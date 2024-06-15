"""• Создайте класс Shape, объекты которого имеют атрибуты Colour –
строка, например, «Красный», «Синий»; Square – площадь
объекта
• Создайте несколько методов:
1. Установить цвет объекта
2. Запросить цвет объекта и напечатать его
3. Задать площадь объекта
4. Запросить площадь объекта"""


class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        print(self.colour)
        return self.colour

    def set_square(self, square):
        self.square = square

    def get_square(self):
        return self.square


room = Shape('Red', 20)  # установили цвет и площадь обькта
room.get_colour()  # получили цвет
room.set_colour('Blue')  # установили новый цвет
print(room.get_square())  # получили площадь
room.set_square(30)  # установили новую площадь
room.get_colour()  # получили цвет(новый)
print(room.get_square())  # получили площадь(новую)
