word = input('Введите слово: ')
letters = list(word)
print(letters)

count_unique = 0
count_unique_2 = 0
for i in letters:
    if letters.count(i) == 1:
        count_unique += 1
print('Кол-во уникальных букв:', count_unique)