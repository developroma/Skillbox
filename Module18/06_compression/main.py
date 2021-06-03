string = input('Введите строку: ')
count = 1
letters = ''
for i in range(len(string)):
    if string[i] == string[i - 1]:
        count += 1
    else:
        letters += string[i - 1] + str(count)
        count = 1
print('Закодированная строка:', letters[2:] + letters[:2])