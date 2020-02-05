# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_line = []
with open ('text 5.6.txt', 'r') as f:
    for i in f.readlines():
        my_line.append(i)

import re

for line in my_line:
    hours = re.findall(r'\d+', line)
    print(
        line.split(':')[0],
        sum([int(h) for h in hours])
    )