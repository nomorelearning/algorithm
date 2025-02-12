T = int(input())
for t in range(1,T+1):
    n,cnt = map(int,input().split())
    state = list(map(int,input()))


def updown(lst, i):
    if lst[i-1] == lst[i+1] == 1:
        lst[i - 1] = 0, lst[i + 1] =0
    elif lst[i-1] == lst[i+1] == 0:
        lst[i - 1] =1, lst[i + 1] = 1
