count_orders = int(input('Введите кол-во заказов: '))

names_dict = dict()
orders_dict = dict()
count_pizza = 0
for i_orders in range(1, count_orders + 1):
    name, order, quantity = input(f'{i_orders} заказ: ').split()
    if not order in orders_dict:
        names_dict[name] = orders_dict
        orders_dict[order] = quantity
        count_pizza = int(quantity)
    else:
        count_pizza += int(quantity)
        orders_dict[order] = count_pizza
print(names_dict)
