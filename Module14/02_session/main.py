print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x2 - x1
y_diff = y2 - y1
if x_diff > 0 or y_diff > 0:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Уравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
elif x_diff == 0 or y_diff == 0:
    print('X', x_diff, 'Y', ,y_diff)