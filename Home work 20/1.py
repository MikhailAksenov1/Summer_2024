"""Человек регулярно приходит в кафе выпить чашку кофе, выбирая
разные варианты кофе, иногда с пирожным, выбирая, что есть в
меню.
Оплачивает иногда наличными деньгами, иногда картой.
Разработайте классы, их атрибуты, свойства и методы.
Может быть какую-то отчетность."""


class Caffe:
    def __init__(self):
        self.menu = {'Авторский кофе': 3600, 'Американо': 100, 'Капучино': 150, 'Раф': 200, 'Латте': 350,
                     'пироженое картошка': 80, 'Пироженое наполеон': 100, 'Слойка': 125}
        self.kassa = 1000  # деньги в кассе
        self.terminal = 0

    def take_order(self, order):
        print(order)
        self.check = []
        self.result = 0  # итоговая сумма за заказ
        for i in order:
            if i in self.menu:
                self.result += self.menu[i]
                self.check.append({i: self.menu[i]})
        print(self.check)

    def pay(self, customer, money, card=False):
        if card:
            self.terminal += self.result
            customer.give_money(self.result)
        else:
            if money == self.result:
                self.kassa += money
                customer.give_money(money)
            elif money > self.result:
                self.kassa += money
                self.kassa = self.kassa - (money - self.result)
                customer.give_money(money)
                customer.take_money(money - self.result)


class Customer:
    def __init__(self, money):
        self.money = money

    def give_money(self, money):
        self.money -= money

    def take_money(self, money):
        self.money += money


cust = Customer(10000)
Starbucks = Caffe()
order = input().split(',')  # Американо,Слойка
Starbucks.take_order(order)
Starbucks.pay(cust, 1000, card=True)
print(cust.money)
