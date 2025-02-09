lst = list(range(1, 31))

for _ in range(28):
    data = int(input())
    lst[data-1] = 0
    
for i in range(30):
    if lst[i] != 0:
        print(lst[i])