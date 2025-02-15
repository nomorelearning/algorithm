import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_sum = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            now = 0
            for i in range(m):
                for j in range(m):
                    now += arr[r+i][c+j]
            if now > max_sum:
                max_sum = now

    print(f'#{t} {max_sum}')