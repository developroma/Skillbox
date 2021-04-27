def summ_n(n):
    summ = 0
    while n != 0:
        last = n % 10
        n //= 10
        summ += last
    return summ

def count_n(n):
    count = 0
    while n != 0:
        last_n = n % 10
        n //= 10
        count += 1
    return count

n = int(input('Введите число: '))

print('\nСумма чисел:', summ_n(n))
print('Кол-во чисел в числе:', count_n(n))
print('Разность суммы и кол-ва чисел:', summ_n(n) - count_n(n))