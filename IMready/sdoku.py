import sys
sys.stdin = open('test.txt')

def sdok(arr):
    for r in range(9):      # 가로로 중복 값 있는지 확인
        lst = []
        for c in range(9):
            if arr[r][c] in lst:
                return 0
            lst.append(arr[r][c])
    for c in range(9):      # 세로로 중복 값 있는지 확인
        lst = []
        for r in range(9):
            if arr[r][c] in lst:
                return 0
            lst.append(arr[r][c])
    for r in [0,3,6]:       # 3x3으로 중복 값 있는지 확인
        for c in [0,3,6]:
            lst = []
            for i in range(3):
                for j in range(3):
                    if arr[r+i][c+j] in lst:
                        return 0
                    lst.append(arr[r][c])
    return 1        # 전부 없으면 1 출력

T = int(input())
for t in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{t} {sdok(arr)}')