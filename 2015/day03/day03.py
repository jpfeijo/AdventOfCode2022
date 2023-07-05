visited_houses = set()
x = y = xr = yr = 0  

visited_houses.add((x, y))  

with open('2015/day03/input.txt') as file:
    for line in file:
        for i, char in enumerate(line):
            if i % 2 == 0:
                if char == '>':
                    x += 1
                elif char == '<':
                    x -= 1
                elif char == '^':
                    y += 1
                elif char == 'v':
                    y -= 1
                visited_houses.add((x, y))
            
            else:  
                if char == '>':
                    xr += 1
                elif char == '<':
                    xr -= 1
                elif char == '^':
                    yr += 1
                elif char == 'v':
                    yr -= 1
                visited_houses.add((xr, yr))

print(len(visited_houses))