def lcd(num):
    i = 1
    while i < num:
        i += 1
        if num % i == 0:
            return i

n = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', lcd(n))