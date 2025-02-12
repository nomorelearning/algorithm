import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_val = 0
    min_val = 10e9
    for r in range(n):
        for c in range(n):
            result = -arr[r][c]
            for k in range(n):
                result += arr[r][k]
                result += arr[k][c]
            if max_val < result:
                max_val = result
            if min_val > result:
                min_val = result
    print(f'#{t} {max_val-min_val}')