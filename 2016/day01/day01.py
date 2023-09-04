with open('2016/day01/input.txt') as file:
    for line in file:
        instructions = line.split(', ')

x, y = 0, 0
dx, dy = 0,  1

for instruc in instructions:
    turn, steps = str(instruc[0]), int(instruc[1:])

    if turn == 'R':
        dx, dy = dy, -dx
    else:
        dx, dy = -dy, dx

    x += dx * steps
    y += dy * steps


distance = abs(x) + abs(y)

print(distance)
