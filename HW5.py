profit = int(input('Введите прибыль предприятия:'))
loss = int(input('Введите сумму убытков:'))

if profit>loss:
    print('Работали в прибыль')
    rent = profit / (profit - loss)
    print(f'Рентабельность выручки составляет: {rent}')
    workers = int(input('Сколько у вас работников на предприятии?'))
    result = (profit - loss)/workers
    print(f'Прибыль на сотрудника составляет {result}')
elif profit==loss:
    print('Работали в ноль')
else:
    print('Работал в убыток')


