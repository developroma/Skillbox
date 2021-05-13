count_people = int(input('Кол-во человек: '))
counting_number = int(input('Какое число в считалке?: '))
print('Значит, выбывает каждый', counting_number, 'человек')

list_people = list(range(1, count_people + 1))

while len(list_people) != 1:
    for i in range(len(list_people)):
        print('Текущий круг людей:', list_people)
        print('Начало счёта с номера', i + 1)
        print('Выбывает человек под номером:', counting_number - len(list_people) - 1)
        list_people.remove(list_people[counting_number - len(list_people) - 1 * len(list_people)])
