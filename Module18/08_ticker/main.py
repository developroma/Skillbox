fst_string = input('Первая строка: ')
second_string = input('Вторая строка: ')

clone_fst_string = fst_string[:]
clone_fst_string *= 2

if second_string in clone_fst_string:
    shift = clone_fst_string.index(second_string)
    print('Первая строка получается из второй со сдвигом {shift}'.format(shift=shift))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
