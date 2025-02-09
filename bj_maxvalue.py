max_val = 0
max_idx = -1

for idx in range(1,10):
    val = int(input())
    if val > max_val:
        max_val = val
        max_idx = idx

print(max_val)
print(max_idx)