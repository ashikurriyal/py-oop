n = int(input())
a = input().split()      # list of strings, e.g. ['2', '4', '1', '4', '2']

# Step 1: count how many times each number appears
counts = {}
for item in a:
    x = int(item)
    if x in counts:
        counts[x] = counts[x] + 1
    else:
        counts[x] = 1

# Step 2: decide how many to remove for each number
removed = 0
for x in counts:
    count = counts[x]
    if count >= x:
        removed = removed + (count - x)   # remove only the extras
    else:
        removed = removed + count         # not enough copies, remove all

print(removed)