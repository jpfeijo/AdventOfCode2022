with open('2016/day01/input.txt') as file:
    for line in file:
        instructions = line.split(', ')

visited = set()
x, y = 0, 0
dx, dy = 0,  1

for instruc in instructions:
    turn, steps = instruc[0], int(instruc[1:])
    if turn == "R":
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx

    for _ in range(steps):
        x += dx
        y += dy

        if (x, y) in visited:
            distance = abs(x) + abs(y)
            print(distance)
            break

        visited.add((x, y))
