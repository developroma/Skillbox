shift = int(input('Сдвиг: '))
old_list = list(input('Изначальный список: '))

print('Изначальный список:', old_list)

old_list.insert(0, old_list[-1 * shift])
old_list.pop(-1 * shift)
print('Сдвинутый список:', old_list)