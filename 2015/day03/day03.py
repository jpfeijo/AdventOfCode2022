visited_houses = set()
x = y = 0

visited_houses.add((x, y))

print(visited_houses)

with open('2015/day03/input.txt') as file:
    for line in file:
        for char in line:
            if char == '>':
              x += 1

            if char == '<':
              x -= 1

            if char == '^':
              y += 1

            if char == 'v':
                y -= 1

            visited_houses.add((x, y))

print(len(visited_houses))