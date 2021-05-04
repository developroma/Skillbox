count_containers = int(input('Кол-во контейнеров: '))
containers = []

for count in range(count_containers):
    weight_containers = int(input('Введите вес контейнера: '))
    containers.append(weight_containers)

weight_new_containers = int(input('Введите вес нового контейнера: '))

s = 0
for i in containers:
    s += 1

print('Номер, контейнера куда встанет новый контейнер:', s)