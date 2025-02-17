def find_upground(lst):
    idx = [0]
    now = 0
    while now < len(lst):
        if lst[now] > lst[now + 1]:
            idx.append(now+1)
        now += 1
    return idx