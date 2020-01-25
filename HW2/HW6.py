#Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
base = [
    (1, {"название": "комрьютер", "цена": 60000, "количество": 5, "ед. измерения": "шт."}),
    (2, {"название": "принтре", "цена": 10000, "количество": 3, "ед. измерения": "шт."}),
    (3, {"название": "сканер", "цена": 4000, "количество": 7, "ед. измерения": "шт."})]
user = input("Что вы хотите узнать?")
result_1 = base [0][1][user]
result_2 = base [1][1][user]
result_3 = base [2][1][user]
result = [result_1, result_2, result_3]
print(f'{user}: {result}')


