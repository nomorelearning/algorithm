import sys
sys.stdin = open('test.txt')

T = int(input())
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for t in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for r in range(n):
        for c in range(m):
            now = arr[r][c]
            for d in range(4):
                for l in range(1, arr[r][c]+1):
                    nr = r + l*dr[d]
                    nc = c + l*dc[d]
                    if 0 <= nr < n and 0 <= nc < m:
                        now += arr[nr][nc]
            if now > result:
                result = now
    print(f'#{t} {result}')