# import sys
# sys.stdin = open('test.txt')
#
# T = int(input())
# for t in range(1,T+1):
#     n = int(input())
#     arr = [list(map(int,input().split())) for _ in range(n)]
#     # 부분집합 만들기(길이가 N/2)
#     comb = []
#     for i in range(1<<n):
#         cnt = 0
#         hap = []
#         hap2 = []
#         for j in range(n):
#             if i & (1<<j):
#                 if cnt == n/2:
#                     break
#                 hap.append(j)
#
#         if hap in hap2:
#             continue
#         hap2.append([x for x in range(n) if x not in hap])
#         comb.append(hap)
#     for r in comb