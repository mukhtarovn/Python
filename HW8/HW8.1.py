#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
#  должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#  Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#  Проверить работу полученной структуры на реальных данных.
import datetime

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date1 = [day, month, year]
        for i in date1:
            print(i)

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        print (day <= 31 and month <= 12 and year <= 3999)

date2 = Date.from_string(datetime.datetime.now().strftime('%d-%m-%Y'))
is_date = Date.is_date_valid(datetime.datetime.now().strftime('%d-%m-%Y'))









