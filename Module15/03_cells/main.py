count_cells = int(input('Кол-во клеток: '))
cells = []
c = []

for i in range(1, count_cells + 1):
    print('Эффективность', i, 'клетки: ', end='')
    efficiency = int(input())
    cells.append(efficiency)
    if i > cells[i - 1]:
        c.append(cells[i - 1])
print('Неподходящие значения:', c)