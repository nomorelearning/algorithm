N = int(input())
min_val = 10e6
max_val = -10e6
lst = list(map(int,input().split()))

for i in lst:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i
        
print(min_val, max_val)