# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import math


with open('text5.3.txt', 'r') as file:
    solarys = []
    workers = 0
    for line in file:
        name, solary = line.split()
        solarys.append(float(solary))
        workers +=1
        if float(solary) < 20000:
            print (f'У {name}а зарплата меньше 20 тыс')
    print(f'Средняя величина дохода сотрудников составляет {sum(solarys)/workers}')

