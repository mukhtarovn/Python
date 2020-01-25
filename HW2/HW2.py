my_list = []
len_list = int(input('Сколько элементов будет содержать список?: '))
while len(my_list)<len_list:
    my_list.append(input('Введи элемент списка: '))

for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)
