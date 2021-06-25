count_words = int(input('Введите кол-во пар слов: '))

synonyms_dict = dict()
for i in range(count_words):
    pars = input(f'{i + 1} пара: ').lower().split(' - ')
    synonyms_dict[i + 1] = pars
    seek_words = input('Введите слово: ').lower()
    for i_list in range(len(pars)):
        if synonyms_dict[i + 1][i_list] == seek_words:
            print('Синоним:', synonyms_dict[i + 1][-i_list + 1])
        else:
            print('Такого слова в словаре нет.')