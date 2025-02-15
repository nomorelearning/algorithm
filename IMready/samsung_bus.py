import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    p = int(input())
    result = []
    for _ in range(p):
        station = int(input())
        count = 0
        for r in range(n):
            if arr[r][0] <= station <= arr[r][1]:
                count += 1
        result.append(count)
    print(f'#{t}', *result)