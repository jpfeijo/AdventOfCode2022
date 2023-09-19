def is_larger(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[0] + sorted_sides[1] > sorted_sides[2]


triangles = 0
columns = [[], [], []]

with open('2016/day03/input.txt') as file:
    for line in file:
        triangle = list(map(int, line.split()))
        for i in range(3):
            columns[i].append(triangle[i])

for column in columns:
    for i in range(0, len(column), 3):
        triangle = column[i:i+3]
        if is_larger(triangle):
            triangles += 1

print(triangles)
