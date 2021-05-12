guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

enter_or_exit = 0
while enter_or_exit != 'Пора спать':
    if len(guests) <= 6:
        print('Сейчас на вечеринке ', len(guests), ' человек:', guests)
        enter_or_exit = input('Гость пришел или ушел?: ')
        name_guest = input('Имя гостя: ')
        if enter_or_exit == 'пришел':
            guests.append(name_guest)
            print('Привет,', name_guest + '!')
        elif enter_or_exit == 'ушел':
            guests.remove(name_guest)
            print('Пока,', name_guest + '!')
    else:
        print('Прости,', name_guest, ', но мест нет.')
        break
else:
    print('Вечеринка закончилась все легли спать')