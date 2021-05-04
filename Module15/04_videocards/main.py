count_video = int(input('Кол-во видеокарт: '))

old_list = []
new_list = []

for i in range(1, count_video + 1):
    print(i, 'Видеокарта: ', end='')
    model_video = int(input())
    old_list.append(model_video)
for i in old_list:
    max_model_video = max(old_list)
    if max_model_video != i:
        new_list.append(i)
print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)

