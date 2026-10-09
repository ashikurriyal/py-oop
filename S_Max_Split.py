s = input()

balance = 0     
current = ""
pieces = []

for ch in s:
    current = current + ch

    if ch == 'L':
        balance = balance + 1
    else:
        balance = balance - 1
   
    if balance == 0:
        pieces.append(current)
        current = ""

print(len(pieces))
for p in pieces:
    print(p)