N, M =map(int,input().split())

lst = [0] * N
for i in range(M):
    start, end, what = map(int,input().split())
    for j in range(start-1, end):
        lst[j] = what
    
print(*lst)