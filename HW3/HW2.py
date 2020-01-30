# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

# вариант 1
def info (**kwargs):
    result =''
    for key, value in kwargs.items():
        result += f'{key}: {value} '
    return result

my_info = {
    'name':'Nariman',
    'surname':'Mukhtarov',
    'date':'19.03.1985',
    'city':'Moscow',
    'email':'mukhtarov.n@gmail.com'
}

print(info(**my_info))

# Вариант №2

def user_info (name, age, city, email):
    a = print (name +', ' + age + ' год(а)' + 'живет в городе ' + city + ', ' + email)
    return a

print (user_info ('Nariman', '19.03.1985', 'Moscow', 'mukhtarov.n@gmail.com'))
