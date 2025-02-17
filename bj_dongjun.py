n = int(input())
arr = []
total = 0
for i in range(n):
    arr.append(int(input()))
for i in range(n-2,-1,-1):
    if arr[i] >= arr[i+1]:
        sum_val = arr[i]-arr[i+1]+1
        arr[i] -= sum_val
        total += sum_val

print(total)