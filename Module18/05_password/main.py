count = 0

while True:
    password = input('Придумайте пароль: ')
    for i_2 in password:
        if i_2.isdigit():
            count += 1

    for i in password:
        if len(password) >= 8 and i.isupper() and count >= 3:
            print('Это надёжный пароль!')
            break
        else:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
            break