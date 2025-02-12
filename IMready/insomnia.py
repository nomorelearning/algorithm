
T = int(input())
for t in range(1, T+1):
    num = int(input())
    lst = []
    cnt = 0
    k = 1
    while cnt < 10:
        data = list(str(num * k))
        for i in data:
            if i not in lst:
                lst.append(i)
                cnt += 1
            if cnt == 10:
                break
        k += 1
    print(f'#{t} {(k-1)*num}')