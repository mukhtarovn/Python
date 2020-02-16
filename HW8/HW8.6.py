"""Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""

class Store:

    def __init__(self, name):
        self.name = name
        self.__goods = []

    def add_app(self, tech):
        self.__goods.append(tech)
    def __getitem__(self, item):
        return self.__goods[item]
    def __str__(self):
        return

class Appliances(Store):
    def __init__(self, name, color, quantity):
        self.name = name
        self.color = color
        self.quantity = quantity
    def __str__(self):
        return f'{self.name}, цвет - {self.color}, количество -- {self.quantity}'


class Printer(Appliances, Store):
    def __init__(self, name, color, quantity, print_speed):
        super().__init__(name, color, quantity)
        self.print_speed = print_speed
class Scaner (Appliances):
    def __init__(self, name, color, quantity, options):
        super ().__init__ (name, color, quantity)
        self.options = options
class Xerox (Appliances):
    def __init__(self, name, color, quantity, size):
        super().__init__(name, color, quantity)
        self.size = size

p = Printer('Samsung', 'Black', 20, '40 л/мин')
s = Scaner('Canon', 'Gray', 30, True)
x = Xerox ('Xerox', 'White', 10, 'a4')
a = Store('Склад')
a.add_app(x)
a.add_app(s)
print(a[0])
