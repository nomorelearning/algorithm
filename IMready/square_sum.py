import sys
sys.stdin = open('test.txt')

T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result_idx = []
    # 박스 범위 안의 인덱스를 중복없이 리스트로 묶기
    for i in range(m):
        sr, sc, l = map(int,input().split())
        for r in range(sr, sr + l):
            for c in range(sc, sc + l):
                if r < 0 or r >= n or c < 0 or c >= n:
                    continue
                if (r,c) not in result_idx:
                    result_idx.append((r,c))
    # 리스트 순회하며 값을 합하기
    result = 0
    for idx in result_idx:
        r, c = idx
        result += arr[r][c]

    print(f'#{t}', result)