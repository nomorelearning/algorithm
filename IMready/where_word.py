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

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    possibel_num = 0
    # 행 조사
    for i in range(N):
        count = 0
        for j in range(N):
            if matrix[i][j] == 1:
                count += 1
                if count == K:
                    possibel_num += 1
                if count == K + 1:
                    possibel_num += -1
            else:
                count = 0
        count = 0
        for j in range(N):
            if matrix[j][i] == 1:
                count += 1
                if count == K:
                    possibel_num += 1
                if count == K + 1:
                    possibel_num += -1
            else:
                count = 0
    # 열 조사
    for j in range(N):
        count = 0

    print(f"#{test_case} {possibel_num}")
