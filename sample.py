n, k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for nat1 in range(n-1):
    for nat2 in range(nat1 + 1, n):
        if arr[nat1][1] < arr[nat2][1]:
            arr[nat1], arr[nat2] = arr[nat2], arr[nat1]
        elif arr[nat1][1] == arr[nat2][1]:
            if arr[nat1][2] < arr[nat2][2]:
                arr[nat1], arr[nat2] = arr[nat2], arr[nat1]
            elif arr[nat1][2] == arr[nat2][2]:
                if arr[nat1][3] < arr[nat2][3]:
                    arr[nat1], arr[nat2] = arr[nat2], arr[nat1]
nat = [list(x) for x in zip(*arr)][0]
cnt = -1
for i in range(n):
    if arr[i][1:4] == arr[nat[0].index(k)][1:4]:
        cnt += 1
