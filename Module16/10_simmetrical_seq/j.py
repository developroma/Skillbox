s = [1, 2, 3, 4, 5, 6, 7, 8]
d = []
for i in range(0, len(s)):
    for i1 in range(0, i):
        d.append(s[i1])
print(s)
print(d)