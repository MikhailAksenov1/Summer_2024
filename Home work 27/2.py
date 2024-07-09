"""Необходимо реализовать класс Item, описывающий предмет, конструктор
которого принимает три аргумента:
name — название предмета
price — цена предмета в рублях
quantity — количество предметов
При обращении к атрибуту name экземпляра класса Item будет возвращаться
его название с заглавной буквы, а при обращении к атрибуту total —
произведение цены предмета на его количество."""

class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def total(self):
        return self.price * self.quantity

shop = Item('кеды_Vans', 18500, 10)
print(shop.name)
print(shop.total)