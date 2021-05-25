count_stick = int(input('Кол-во палок: '))
count_shot = int(input('Кол-во бросков: '))
for shots in range(count_shot):
    print('Бросок:', shots + 1, end='')
    left_stick = int(input('Сбиты палки с номера', 'по номер 10'))