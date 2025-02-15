import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for r in range(n):
        length = 0
        for c in range(m):
            if arr[r][c] == 0:
                length = 0
            else:
                length += 1
                if length > ans:
                    ans = length
    for c in range(m):
        length = 0
        for r in range(n):
            if arr[r][c] == 0:
                length = 0
            else:
                length += 1
                if length > ans:
                    ans = length
    print(f'#{t}',ans)