text = 'Это задание очень! простое'
sym = '!'
for i in sym:
    for x in text:
        if i != x:
            pass
        x += i
        print(x)