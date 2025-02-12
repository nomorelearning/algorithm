t = 'TTTTTATTAATA'
p = 'TTA'

def search(t,p):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1

print(search(t,p))


A = 'ABCD'
B = 'EFGHIJKLMN'

N= len(A)
M = len(B)
i = j = 0
ans = ''
while i+j < N+M:
    if i <N:
        ans += A[i]
        i += 1
    if j < M:
        ans += B[j]
        j+=1
print(ans)

i = j = 0
ans = [0]*(N+M)
while i+j < N+M:
    if i < N:
        ans[i+j] = A[i]
        i+= 1
    if j < M:
        ans[i+j] = B[j]
        j+=1
print(''.join(ans))