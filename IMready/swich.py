n = int(input())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))


def check_next(lst, idx):
    if lst[idx + 1] != 1:
        return idx + 1
    else:
        idx += 1
        check_next(lst, idx)
        
diff = [0]*n
for i in range(n):
    if ai[i] != bi[i]:
        diff[i] += 1

def find_diff(diff, i, n):
    while i < n:
        if diff[i] == 1:
            return i
        else:
            i += 1

result = 0
idx = 0
while idx < n:
    idx = find_diff(diff, idx, n)
    result += 1
    if idx != n:
        idx = check_next(diff, idx)