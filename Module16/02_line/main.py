first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))

first_class.extend(second_class)

for i in range(len(first_class)):
    for i_min in range(i, len(first_class)):
        if first_class[i] > first_class[i_min]:
            first_class[i_min], first_class[i] = first_class[i], first_class[i_min]

print('Отсортированный список:', first_class)