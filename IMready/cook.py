import sys
sys.stdin = open('test.txt')

# T = int(input())
# for t in range(1,T+1):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#
#     ingre_idx = []       # 모든 재료 인덱스 넣기
#     for i in range(n-1):
#         for j in range(i+1,n):
#             ingre_idx.append((i,j))
#
#     min_gap = 1e9
#     for r1, c1 in ingre_idx:
#         for idx2 in ingre_idx:
#             if r1 not in idx2 and c1 not in idx2:
#                 r2, c2 = idx2
#                 print(r1, c1, r2, c2)
#                 gap = abs(arr[r1][c1] + arr[c1][r1] - arr[r2][c2] - arr[c2][r2])
#                 if gap < min_gap:
#                     min_gap = gap
#     print(min_gap)