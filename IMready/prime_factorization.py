import sys
sys.stdin = open('test.txt')

bottom = [2, 3, 5, 7, 11]
def prime(n, num):
    ans = 0
    while n > 1:
        if n%num != 0:
            break
        n /= num
        ans += 1
    return ans

T = int(input())
for t in range(1,T+1):
    n = int(input())
    ans = [0] * 5
    i = 0
    while n > 1:
        x = prime(n,bottom[i])
        ans[i] += x
        n /= bottom[i] ** x
        i += 1
    print(f'#{t}',*ans)