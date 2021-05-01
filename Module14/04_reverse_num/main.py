def nums_reverse(num):
    float_part_num = int(num % 1 * 100)
    float_part_num_reverse = 0

    integer_part_num = int(num) // 1
    integer_part_num_reverse = 0
    while float_part_num != 0 or integer_part_num != 0:
        last = float_part_num % 10
        last_2 = integer_part_num % 10
        float_part_num //= 10
        integer_part_num //= 10
        float_part_num_reverse *= 10
        integer_part_num_reverse *= 10
        float_part_num_reverse += last
        integer_part_num_reverse += last_2
    result = float(str(integer_part_num_reverse) + '.' + str(float_part_num_reverse))
    return result


num = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
print('Первое число наоборот:', nums_reverse(num))
print('Второе число наоборот:', nums_reverse(num_2))
print('Сумма:', round(nums_reverse(num) + nums_reverse(num_2), 2))