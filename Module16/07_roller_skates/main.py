count_skates = int(input('Кол-во коньков: '))
skates = []

for size_skates in range(count_skates):
    print('Размер', size_skates + 1, 'пары: ', end='')
    size_of_pair_skates = int(input())
    skates.append(size_of_pair_skates)

count_people = int(input('Кол-во людей: '))

legs = []
count_people_skates = 0
for size_leg in range(count_people):
    print('Размер ноги', size_leg + 1, 'человека: ', end='')
    size = int(input())
    skates.append(size)
    if skates[-1*count_people] <= skates[count_skates]:
        count_people_skates += 1

print('Наибольшее кол-во людей, которое могут взять ролики:', count_people_skates - 1)