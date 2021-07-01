def is_prime(data):
    return [i for i in data if i >= 2 if i % (i // 2) != 0]


print(is_prime([3, 5, 7, 11, 12, 13, 14]))