count_orders = int(input('Введите кол-во заказов: '))

names_dict = dict()
count_pizza = 0
for i_orders in range(1, count_orders + 1):
    name, order, quantity = input(f'{i_orders} заказ: ').split()
    if name not in names_dict:
        names_dict[name] = dict()
        names_dict[name][order] = quantity
        count_pizza = int(quantity)
    else:
        count_pizza += int(quantity)
        names_dict[name][order] = count_pizza
print(sorted(names_dict))
