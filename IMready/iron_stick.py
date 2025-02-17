import sys
sys.stdin = open('test.txt')
T = int(input())
for t in range(1,T+1):
    sticks = list(input())
    stack = 0
    i = 0
    result = 0
    while i < len(sticks) - 1:
        if sticks[i] == '(':
            if sticks[i+1] == ')':
                result += stack
                i += 2
            else:
                stack += 1
                i += 1
        else:
            stack -= 1
            result += 1
            i += 1
    if sticks[-2] != '(':
        result += stack
    print(f'#{t}',result)