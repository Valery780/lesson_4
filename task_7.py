a = [1, 5, 3, 7, 6]
b = [3, 5, 7, 8, 9]
c = []
for i in a:
    for k in b:
        if i == k:
            c.append(i)
            break
print(c)