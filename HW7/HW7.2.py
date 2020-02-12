# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.)

class Dress:
    def __init__(self, v, h):
        self.v = v
        self.h = h
# для пальто
    def get_consumption_coat(self):
        return round(self.v / 6.5 + 0.5, 2)
# для костюма
    def get_consumption_suit(self):
        return round(self.h * 2 + 0.3, 2)

# Общий расход ткани
    @property
    def get_consumption_full(self):
        return str(f'Площадь общая ткани'
                   f' {round(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')

# Класс одежды пальто
class Coat(Dress):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_c = round(self.v / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Площадь ткани на пальто {round(self.square_c, 2)}'
# Класс одежды костюм
class Suit(Dress):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.square_j = round(self.h * 2 + 0.3 , 2)

    def __str__(self):
        return f'Площадь ткани на костюм {round(self.square_j , 2)}'


Coat = Coat(5, 6)
Suit = Suit(6, 9)

print(Coat)
print(Suit)
print(Coat.get_consumption_full)


