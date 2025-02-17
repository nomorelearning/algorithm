import sys
sys.stdin = open('test.txt')

T = int(input())

for t in range(1,T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in range(5):
        if len(arr[i]) > max_len:
            max_len = len(arr[i])
    word = ''
    for i in range(max_len):
        for j in range(5):
            if len(arr[j]) < i+1:
                continue
            word += arr[j][i]
    print(f'#{t} {word}')