N, M = map(int, input().split())
lst = list(range(1,N+1))

for _ in range(M):
    go, come = map(int, input().split())
    lst[go-1], lst[come-1] = lst[come-1], lst[go-1]

print(*lst)