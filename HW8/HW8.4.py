"""Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
class Store:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Appliances:
    def __init__(self, name, color, quantity):
        self.name = name
        self.color = color
        self.quantity = quantity

class Printer(Appliances):
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





