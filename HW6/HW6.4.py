# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_polis = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_polis
    def go(self):
        return (f'Автомобиль {self.name} поехал.')
    def stop (self):
        return (f'Автомобиль {self.name} остановился.')
    def turn (self, direction):
        return (f'Автомобиль {self.name} повернул на {direction}.')
    def show_speed (self):
        return (f'Ваша скорость{self.speed}.')


class TownCar (Car):
    def show_speed(self):
        if self.speed > 60:
            return ('Превышение скорости!!!')
        else:
            return (f'Ваша скорость {self.speed}.')
class WorkCar (Car):
    def show_speed(self):
        if self.speed > 40:
            return ('Превышаете скорость.')
class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

town = TownCar('BMW', 70, 'Black', False)
print(town.go(), town.turn('лево'), town.show_speed(), town.stop())

sport = SportCar('Lamborgini', 200, 'yellow', False)
print(sport.go(), sport.turn("право"), sport.show_speed(), sport.stop())

work = WorkCar('VW', 50, 'Red', False)
print(work.go(), work.turn('право'), work.show_speed(), work.stop())

police = PoliceCar('Ford', 60, 'blue', True)
print(police.go(), police.turn('лево'), police.show_speed(), police.stop())

