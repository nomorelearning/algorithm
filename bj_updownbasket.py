N, M = map(int, input().split())
baket = list(range(1,N+1))

def updown(lst, start, end):
    long = (end - start + 1) // 2
    for i in range(long):
        lst[i+start-1], lst[end-i-1] = lst[end-i-1], lst[i + start-1]

for _ in range(M):
    start, end = map(int,input().split())
    updown(baket, start, end)    
    
print(*baket)