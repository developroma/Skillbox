string = input('Введите текст: ').lower()
string_dict = dict()

for i in string:
    if i in string_dict:
        string_dict[i] += 1
    else:
        string_dict[i] = 1
print('Оригинальный словарь частот: ')
for i in string_dict.keys():
    print(i, ':', string_dict[i])

print('Инвертированный словарь частот:')
new_dict = dict()
new_list = []
for i in string_dict:
    new_dict[string_dict[i]] = i
    print(new_dict)