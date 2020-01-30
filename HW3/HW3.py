#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    min_n = min(a,b,c)
    sum_n = a+b+c
    result = sum_n-min_n
    return result

print(my_func(200,300,100))