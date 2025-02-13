import sys
sys.stdin = open('test.txt')


def up_sum(n, arr):
    map1 = [list(x) for x in arr]
    map2 = [list(x) for x in zip(*arr)]
    for i in range(n):
        for j in range(1, n):
            if map1[i][j] == 1:
                map1[i][j] += map1[i][j-1]
            if map2[i][j] == 1:
                map2[i][j] += map2[i][j-1]
    return map1, map2

T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    map1, map2 = up_sum(n,arr)

    for i in range(n):
        for j in range(n-1):
            if map1[i][j] == k and map1[i][j+1] == 0:
                cnt += 1
            if map2[i][j] == k and map2[i][j+1] == 0:
                cnt += 1
        if map1[i][n-1] == k:
            cnt += 1
        if map2[i][n-1] == k:
            cnt += 1
    print(f'#{t}',cnt)
