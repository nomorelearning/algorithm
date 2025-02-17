winner = 0
score = 0

for cand in range(1,6):
    lst = list(map(int, input().split()))
    cur_sum = sum(lst)
    if score < cur_sum:
        score = cur_sum
        winner = cand

print(winner, score)