keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]

x, y = 1, 1
password = ''

with open('2016/day02/input.txt') as file:
    for line in file:
        for instruction in line:
            print(instruction, x, y)
            if instruction == 'U' and x > 0:
                x -= 1
            if instruction == 'D' and x < 2:
                x += 1
            if instruction == 'L' and y > 0:
                y -= 1
            if instruction == 'R' and y < 2:
                y += 1
        password = password + keypad[x][y]

print(password)
