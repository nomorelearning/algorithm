import sys
sys.stdin = open('test.txt')
ball = ['(|','|)','()']
T = int(input())
for t in range(1, T+1):
    cnt = 0
    case = input()
    for sort in ball:
        for i in range(len(case)-1):
            if case[i:i+2] == sort:
                cnt += 1
    print(f'#{t}',cnt)
        