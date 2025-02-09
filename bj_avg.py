N = int(input())
lst = list(map(int,input().split()))

max_val = 0
for i in lst:
    if i > max_val:
        max_val = i

for i in range(len(lst)):
    lst[i] /= max_val
    lst[i] *= 100
    
sum = 0
for i in lst:
    sum += i

avg = sum / len(lst)

print(avg)