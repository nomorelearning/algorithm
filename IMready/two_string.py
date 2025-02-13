import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))
    max_val = -10e9         # 최댓값을 저장
    if n < m:               # 길이에 따라 두 케이스로 나눠
        for i in range(m-n+1):
            val = 0
            for j in range(n):
                val += bi[i+j] * ai[j]
            if max_val < val:
                max_val = val
    elif n > m:
        for i in range(n-m+1):
            val = 0
            for j in range(m):
                val += ai[i+j] * bi[j]
            if max_val < val:
                max_val = val
    print(f'#{t}', max_val)