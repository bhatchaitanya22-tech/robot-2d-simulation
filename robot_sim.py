x, y = 0, 0       # robot starting coordinates
distance = 0       # total distance moved
path = [(x, y)]    # keep track of the path

for move in commands:
    if move == 'L':
        x -= 1  # move left
    elif move == 'R':
        x += 1  # move right
    elif move == 'U':
        y += 1  # move up
    elif move == 'D':
        y -= 1  # move down
    else:
        print("Skipped invalid command:", move)
        continue
    distance += 1
    path.append((x, y))  # add new position to path
print("\n--- Simulation Results ---")
print("Final Position:", (x, y))
print("Total Distance Travelled:", distance)
print("Complete Path:", path)


