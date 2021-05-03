films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']


name_film = input('Введите название  фильма: ')
favorite_films = []

for film in films:
    if name_film == film:
        favorite_films.append(name_film)
    else:
        print('Ошибка. ', film, ' в списке нету')

print('Список любимых фильмов:', favorite_films)