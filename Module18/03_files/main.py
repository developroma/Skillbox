sym = '@№$%^&*()'
name = input('Название файла: ')
for i in sym:
    if name.startswith(i):
        print('Ошибка: название начинается на один из специальных символов')
        break
    elif name.endswith('.txt'):
        print('Файл назван верно')
        break
    else:
        print('Ошибка: название начинается на один из специальных символов')