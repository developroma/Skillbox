count_video = int(input('Кол-во видеокарт: '))

old_list = []
new_list = []

new = 0
for i in range(1, count_video + 1):
    print(i, 'Видеокарта: ', end='')
    model_video = int(input())
    old_list.append(model_video)
    new = model_video
    if new < model_video:
        new = model_video
        new_list.append(new)
print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)

