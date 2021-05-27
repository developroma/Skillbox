count_stick = int(input('Кол-во палок: '))
count_shot = int(input('Кол-во бросков: '))

list_stick = ['|' for _ in range(count_stick)]
for shots in range(count_shot):
    left = int(input('Сбиты палки с номера '))
    right = int(input('по номер '))
    print('Бросок', shots + 1, '. Сбиты палки с номера', left, 'по номер', right)
    new_list = ['.' for _ in range(right - left)]
    list_stick[left:right] = new_list

print('Результат:', *list_stick)