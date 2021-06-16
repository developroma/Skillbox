count_country = int(input('Кол-во стран: '))

dict_1 = dict()
for i in range(count_country):
    country = input(f'{i + 1} страна: ').split()

    dict_1[country[0]] = country[1:]

for i_2 in range(3):
    city = input(f'{i_2 + 1} город: ')
    for i_country in dict_1:
        if city in dict_1[i_country]:
            print(f'Город {city} расположен в стране {i_country}')
            break
        else:
            print(f'По городу {city} данных нет')