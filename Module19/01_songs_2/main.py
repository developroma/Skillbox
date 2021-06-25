violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_songs = int(input('Скольок песен выбрать?: '))

all_time = 0
for songs in range(count_songs):
    name_songs = input(f'Название {songs + 1} песни: ')
    all_time += violator_songs[name_songs]
print('Общее время звучания песен:', round(all_time, 2))

