import sys
sys.stdin = open('test.txt')

T = int(input())

for t in range(1,T+1):
    n = int(input())
    lst = list(input().split())
    result = []
    if n % 2 == 0:
        for i in range(n//2):
            result.append(lst[i])
            result.append(lst[n//2 + i])
    else:
        for i in range(n // 2):
            result.append(lst[i])
            result.append(lst[(n // 2) +1+i])
        result.append(lst[n//2])
    print(f'#{t}', *result)