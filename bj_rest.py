lst = []
for _ in range(10):
    data = int(input())
    data %= 42
    if data not in lst:
        lst.append(data)
        
print(len(lst))