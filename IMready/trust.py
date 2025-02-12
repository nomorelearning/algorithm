import sys
sys.stdin = open('test.txt')
T = int(input())
for t in range(1, T+1):
    n, *data = input().split()
    n = int(n)
    who = []        # 버튼을 누르는 로봇 저장
    whe = []        # 버튼 위치 저장
    for i in range(n):
        who.append(data[2*i])
        whe.append(int(data[2*i + 1]))
    b_pos, o_pos = 1, 1
    total = 0
    b_time, o_time = 0, 0
    
    for i in range(n):
        now = who[i]
        target = whe[i]
        if now == 'B':
            if abs(target - b_pos) - b_time <= 0:
                time = 1
            else:
                time = abs(target - b_pos) - b_time + 1
            o_time += time
            b_pos = target
            b_time = 0
        else:
            if abs(target - o_pos) - o_time <= 0:
                time = 1
            else:
                time = abs(target - o_pos) - o_time + 1
            b_time += time
            o_pos = target
            o_time = 0
        total += time
        
    print(f'#{t}', total)