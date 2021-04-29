first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print('Года от ', first_year, 'до ', second_year, 'с тремя одинаковыми числами:')
num = 0
num_2 = 0
num_3 = 0
num_4 = 0
while second_year >= first_year:
    first_year += 1
    num = first_year % 10
    num_2 = first_year % 100 // 10
    num_3 = first_year % 1000 // 100
    num_4 = first_year % 10000 // 1000
    if num == num_2 and num == num_4 and num_2 == num_4:
        print(first_year)
    elif num_3 == num and num_2 == num_3:
        print(first_year)