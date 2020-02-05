# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.



with open('new_f.txt', 'w') as new_file:
    user_str = input('Введите текст: ')
    new_file.write(user_str)
    while user_str:
        if user_str =='':
            break
        else:
            user_str = input ('Введите текст строки: ')
            new_file.write('\n' + user_str)




