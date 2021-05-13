count_friends = int(input('Кол-во друзей: '))
count_debts = int(input('Долговых расписок: '))

all_list = [0]
all_list *= count_friends
for debts in range(count_debts):
    print('\n', debts + 1, 'расписка')
    where = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    count = int(input('Сколько: '))
    all_list[where - 1] += count
    all_list[from_whom - 1] -= count
for i in range(len(all_list)):
    print(i + 1, ':', all_list[i])