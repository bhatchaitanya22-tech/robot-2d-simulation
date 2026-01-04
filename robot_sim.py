x, y = 0, 0
commands = input("Enter commands (L R U D): ").upper()

distance = 0
path = [(x, y)]

for move in commands:
    if move == 'L':
        x -= 1
    elif move == 'R':
        x += 1
    elif move == 'U':
        y += 1
    elif move == 'D':
        y -= 1
    else:
        continue

    distance += 1
    path.append((x, y))

print("Final Position:", (x, y))
print("Distance Travelled:", distance)
print("Path:", path)

