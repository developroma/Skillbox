string = input('Введите строку: ')

string = list(string)

for i in string:
    if string.count('h') >= 2:
        if i == 'h':
            fst_h = string.index('h')
string.remove('h')

for x in string:
    if x == 'h':
        second_h = string.index('h')

print(string['Перевёрнутая строка:', second_h - 1:fst_h - 1:-1])
