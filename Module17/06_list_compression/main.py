import random
len_list = int(input('Введите число: '))

list_n = [random.randint(0, len_list) for _ in range(len_list)]

print('Старый список:', list_n)
for i in list_n:
    if i == 0:
        list_n.remove(0)
        list_n.append(0)
        list_n.remove(0)
print('Новый список:', list_n)

