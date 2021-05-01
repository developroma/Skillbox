import math

print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('Y: '))
radius = int(input('Введите радиус: '))

pythagorean_theorem = math.sqrt(x ** 2 + y ** 2)

if pythagorean_theorem > radius:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')