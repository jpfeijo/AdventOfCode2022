keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]

keypad_ex2 = [['1'],
              ['2', '3', '4'],
              ['5', '6', '7', '8', '9'],
              ['A', 'B', 'C'],
              ['D']]

x, y = 2, 0
password = ''

with open('2016/day02/input.txt') as file:
    for line in file:
        for instruction in line:
            if instruction == 'U':
                if x == 1 and y == 1:
                    x -= 1
                    y = 0
                elif x == 2 and y != 0 and y != 4:
                    x -= 1
                    y -= 1
                elif x > 2:
                    x -= 1
                    y += 1

            if instruction == 'D':
                if x == 3 and y == 1:
                    x += 1
                    y = 0
                elif x == 2 and y != 0 and y != 4:
                    x += 1
                    y -= 1
                elif x < 2:
                    x += 1
                    y += 1

            if instruction == 'L':
                if (x >= 1 and x <= 3) and y != 0:
                    y -= 1

            if instruction == 'R':
                if (x >= 1 and x <= 3) and y < len(keypad_ex2[x]) - 1:
                    y += 1

            print(instruction, x, y, keypad_ex2[x][y])

        password = password + keypad_ex2[x][y]

print(password)
