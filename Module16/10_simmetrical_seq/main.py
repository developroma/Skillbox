count_n = int(input('Кол-во чисел: '))
list_nums = []
list_add_nums = []
s = 1
for nums in range(count_n):
    num = int(input('Число: '))
    list_nums.append(num)
print('Последовательность:', *list_nums)

while list_nums[-1] == list_nums[-2]:
    list_nums.remove(list_nums[-1])
for nums in range(len(list_nums)):
    list_add_nums.append(list_nums[-1 * nums])
print('Нужно приписать:', len(list_add_nums))
print('Сами числа:', *list_add_nums)