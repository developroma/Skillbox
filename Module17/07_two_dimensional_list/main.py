big_list = []
for i in range(4):
    list_nums = [x + i for x in range(1, 10, 4)]
    big_list.extend([list_nums])
print(big_list)