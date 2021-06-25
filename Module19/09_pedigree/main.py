count_peoples = int(input('Введите количество человек: '))
main_dict = dict()
new_dict = dict()

for i in range(1, count_peoples):
    kid, parent = input(f'{i} пара: ').split()
    main_dict[parent] = kid
    new_dict[kid] = 0
    new_dict[parent] = 0
    if parent in main_dict:
        new_dict[kid] += 1
    elif kid in main_dict:
        new_dict[kid] += 1
        new_dict[parent] += 1

print('"Высота" каждого члена семьи')
for i in new_dict:
    print(i, new_dict[i])