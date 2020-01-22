seconds = int (input('Сколько секунда Вы хотите перевести в часовой формат?:'))
hours = seconds // 3600
seconds %=3600
minutes = seconds//60
seconds %= 60


print(f'{hours} часов, {minutes} минут, {seconds} секунд')