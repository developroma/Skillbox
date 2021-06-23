max_num = int(input('Введите максимальное число: '))
need_nums_set_add = set()
all_answer = ''

while True:
    need_nums = input('Нужное число есть среди вот этих чисел: ').split()
    answer = input('Ответ Артёма: ')
    need_nums_set = set(need_nums)
    if answer == 'Помогите!':
        break
    elif answer == 'Да':
        for i in need_nums:
            need_nums_set_add.add(i)
    elif answer == 'Нет!':
        intersection = need_nums_set_add.intersection(need_nums_set)
        all_answer = need_nums_set_add - intersection
print('Артём мог загадать эти числа:', all_answer)