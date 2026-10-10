s = input()

balance = 0      # +1 for 'L', -1 for 'R'
current = ""     # the piece we are building right now
pieces = []      # list to store all balanced pieces

for ch in s:
    current = current + ch     # add this character to the current piece

    if ch == 'L':
        balance = balance + 1
    else:
        balance = balance - 1

    # balance is 0 means equal L and R, so this piece is balanced
    if balance == 0:
        pieces.append(current)   # save the piece
        current = ""             # start a new empty piece

print(len(pieces))
for p in pieces:
    print(p)