import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    n = int(input())
    lst = list(map(int, input()))
    for i in range(1, n):
        if lst[i] == 1:
            lst[i] += lst[i-1]
    print(f'#{t} {max(lst)}')