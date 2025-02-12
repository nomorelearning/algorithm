import sys
sys.stdin = open('test.txt', 'r')

T = int(input())

def on_off(lst, start):
    for i in range(start, len(lst)):
        if lst[i] == 1:
            lst[i] = 0
        else:
            lst[i] = 1
    return lst

for t in range(1,T+1):
    n = int(input())
    ai = list(map(int, input().split()))
    bi = list(map(int, input().split()))

    cnt = 0

    for i in range(n):
        if ai[i] != bi[i]:
            ai = on_off(ai, i)
            cnt += 1
    if cnt == 0:
        cnt = 2
    print(f'#{t}',cnt)
