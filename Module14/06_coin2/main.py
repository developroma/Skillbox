print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
radius = int(input('Введите радиус: '))

if x > radius and y > radius:
    print('Монетки нет в области')
else:
    print('Монетка где-то рядом')