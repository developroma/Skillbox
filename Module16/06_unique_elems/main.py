list_a = list(input('Введите 3 числа в первый список: '))
list_b = list(input('Введите 7 чисел во второй список: '))

print('Первый список:', list_a)
print('Второй список:', list_b)

list_a.extend(list_b)

new_list = []
for i in list_a:
    if list_a.count(i) >= 2:
        list_a.remove(i)
list_a.remove(list_a[0])
print(list_a)