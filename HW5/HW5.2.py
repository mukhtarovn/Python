# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


file = open ('text5.2.txt', 'r')
line = 0
for i in file:
    line += 1
    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print (i, len (i), 'симв.', word, 'сл.')

print (line, 'стр.')
file.close ()
