import sys
sys.stdin = open('test.txt')

T = int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for t in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    for r in range(n):
        for c in range(m):
            result = arr[r][c]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m:
                    result += arr[nr][nc]
            if result > max_sum:
                max_sum = result
    print(f'#{t}',max_sum)