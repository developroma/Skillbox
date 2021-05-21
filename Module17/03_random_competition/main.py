import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
wins_list = [fst_team[i] if fst_team[i] > second_team[i] else second_team[i] for i in range(20)]
print('Первая команда:', fst_team)
print('Вторая команда:', second_team)
print('Победители тура:', wins_list)