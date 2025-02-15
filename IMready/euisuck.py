import sys
sys.stdin = open('test.txt')

T = int(input())

for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    new = [['*'] * max_len for _ in range(5)]
    print
    for i in range(5):
        j = 0
        while j < len(arr[i]):
            new[i][j] = arr[i][j]
    print(new)
    