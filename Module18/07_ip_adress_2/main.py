ip = input('Введите IP: ').split('.')
new_ip = '.'.join(ip)
count_but = 0

for x in new_ip:
    if x == '.':
        count_but += 1

d = False
f = False
c = False
for i in ip:
    if i.isdigit():
        if int(i) > 255:
            print('{error} превышает 255'.format(error=i))
        else:
            d = True
    elif not i.isdigit():
        print('{error} не целое число'.format(error=i))
    if i.isdigit():
        c = True
if count_but != 3:
    print('Адрес - это четыре числа, разделенные точками')
elif count_but == 3:
    f = True
if d and f and c:
    print('IP-адрес корректен')