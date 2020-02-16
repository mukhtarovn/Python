# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Div(Exception):
    while True:
        user = input ('Введите число на которое гужно разделить число 100: ')
        user = int (user)
        def __init__(self, user):
            self.user = user
        try:
            if user<0:
                print ("Вы ввели отрицательное число")
            else:
                user = int(user)
                print(100/user)
                break
        except TypeError:
            print("Вы ввели не число")
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except ValueError:
            print('Вы ввели не число')





