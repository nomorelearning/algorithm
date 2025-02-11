import sys
sys.stdin = open('test.txt', 'r')

T = int(input())

for t in range(1,T+1):
    n = int(input())
    ai = list(map(int,input().split()))
    bi = list(map(int,input().split()))

    i = n-1
    count = 0
    
    while i > 0:
        if ai[i] == bi[i]:
            if ai[i-1] != bi[i-1]:
                count += 1
        else:
            if ai[i-1] == bi[i-1]:
                count += 1
        i -= 1
    
    if ai != bi and count == 0:
        count = 1
        
    print(f'# {t} {count}')