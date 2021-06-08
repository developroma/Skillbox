# Это задание очень! простое.
list_text = list(input('Сообщение: '))
sym = '!.'
add_list = []
s = []


for i_text in list_text:
    for i_sym in sym:
        if i_sym in i_text:
            index_sym = list_text.index(i_sym)
            delete_sym = list_text.pop(index_sym)
            reverse = list_text[::-1]
            reverse_join = ''.join(reverse)
            new_reverse = reverse_join.split()
            for i_new in range(len(new_reverse)):
                add_list.insert(i_new, new_reverse[-1 * (i_new + 1)])
                new_reverse_2 = ' '.join(add_list)
            for i in new_reverse_2:
                s.append(i)
            s.insert(index_sym, delete_sym)
print(''.join(s))