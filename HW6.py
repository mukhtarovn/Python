a = int(input('Сколько ты пробежал в первый день?:'))
b = int(input('Какой результат вы хотите?:'))
day = 1
print(f'{day}-й день: {round(a,2)} км')
while a < b:
    a = a + a * 0.1
    day +=1
    print(f'{day}-й день: {round(a,2)} км')
print(f'Результат будет достигнут на {day} день')
