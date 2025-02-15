import sys
sys.stdin = open('test.txt')

T = int(input())

for t in range(1,T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    max_idx, min_idx = 0,0
    max_val, min_val = 0, 10
    for i in range(n):
        if lst[i] >= max_val:
            max_val = lst[i]
            max_idx = i
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
    print(f'#{t} {abs(max_idx-min_idx)}')