def is_larger(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[0] + sorted_sides[1] > sorted_sides[2]


triangles = 0

with open('2016/day03/input.txt') as file:
    for line in file:
        triangle = list(map(int, line.split()))
        if is_larger(triangle):
            triangles += 1

print(triangles)
