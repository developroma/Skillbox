text = input('Введите текст: ')
text_1 = list(text)

vowel_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

result_list = [i for i in text for x in vowel_list if i == x]
print('Список гласных букв:', result_list)
print('Длина списка:', len(result_list))