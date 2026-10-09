n = int(input())
a = input().split()

counts = {}
for item in a:
    x = int(item)
    if x in counts:
        counts[x] = counts[x] + 1
    else:
        counts[x] = 1

removed = 0
for x in counts:
    count = counts[x]
    if count >= x:
        removed = removed + (count - x)
    else:
        removed = removed + count

print(removed)