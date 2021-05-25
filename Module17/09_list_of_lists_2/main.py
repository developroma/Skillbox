nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

two_d_list = sum(nice_list, [])
result = []
for i in two_d_list:
    for three_d_list in i:
        result.append(three_d_list)
print(result)