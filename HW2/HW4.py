

user = input("Введите строку из нескольких слов")
n=1
for i in user.split():
    print(f'{n}. {i[:10]}')
    n += 1
