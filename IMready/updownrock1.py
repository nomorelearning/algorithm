import sys
sys.stdin = open('test.txt')

def chage(lst, i, j, n):
    for k in range(1,j):
        if i+k > n:
            break
        lst[i+k-1] = lst[i-1]
        
T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    state = list(map(int,input().split()))
    for _ in range(m):
        i, j = map(int,input().split())
        chage(state, i, j, n)
    print(f'#{t}', *state)