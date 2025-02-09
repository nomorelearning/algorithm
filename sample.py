lst = []
for i in range(23):
    data = input()
    lst.append(data)

middle = ['inf', 'int', 'isf', 'ist', 'enf', 'ent', 'esf', 'est']
count = [0] * 8

for data in lst:
    for i in range(8):
        if middle[i] in data:
            count[i] += 1
            break

print(count)