text = input('Введите строку: ').split()
max_list = [len(i) for i in text]
print(max(max_list))