name_details = input('Название детали - ')

shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count_details = 0
sum_details = 0
for i in range(len(shop)):
    if shop[i][0] == name_details:
        count_details += 1
        sum_details += shop[i][1]
print('\nКол-во деталей - ', count_details)

print('Общая стоимость - ', sum_details)
