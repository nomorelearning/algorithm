import sys
sys.stdin = open('test.txt')

def updown(lst, i, j, n):
    for k in range(1, j+1):
        if i-k <= 0 or i+k > n:
            break
        if lst[i-k-1] == lst[i+k-1]:
            if lst[i-k-1] == 1:
                lst[i-k-1] = 0
                lst[i+k-1] = 0
            else:
                lst[i-k-1] = 1
                lst[i+k-1] = 1
                

T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    state = list(map(int,input().split()))
    for _ in range(m):
        i, j = map(int,input().split())
        updown(state, i, j, n)
    print(f'#{t}', *state)