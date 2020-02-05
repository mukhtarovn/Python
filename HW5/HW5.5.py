# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import math

with open ('text5.5.txt', 'w') as f:
    f.write('4 5 3 8 7')

with open('text5.5.txt', 'r') as fr:
    res = []
    for i in fr.readline():
        if i.isdecimal():
            res.append (int (i))
    print(sum(res))
