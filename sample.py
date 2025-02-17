n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr_re = [list(x) for x in zip(*arr)]
head = 0
for medal in range(1,4):
    for nat in range(n):
        if arr[nat][medal] > arr[arr_re[0].index(k)][medal]:
            head += 1
            arr[nat] = [0] * 4
print(head)