#Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

#Вариант 1
x = abs(int(input('Введите число:')))

y = int(input('введите отрицательное число'))
if y > 0:
    y = y-y*2
elif y == 0:
    print('Только не ноль!!!')

def my_func(x,y):
    return x**y

print(my_func(x,y))

#Вариант 2
def my_func_2(x,y):
    i = y
    res = 1
    while i<0:
        res = res*x
        i+=1
    return 1/res

print(my_func_2(x,y))
