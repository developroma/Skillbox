word = input('Введите слово: ')
letters = list(word)

count = 0
с = 0
for i in letters:
    for i_2 in letters:
        if i_2 == i:
            count += 1
            print(count)