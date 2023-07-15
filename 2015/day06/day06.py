def part_one():
    light_grid = [[False for _ in range(1000)] for _ in range(1000)]
    lights_on = 0

    with open('2015/day06/input.txt') as file:
        for line in file:
            command = line.split()
            action = command[0]

            if action == 'toggle':
                start = [int(x) for x in command[1].split(',')]
                end = [int(x) for x in command[3].split(',')]
            else:
                start = [int(x) for x in command[2].split(',')]
                end = [int(x) for x in command[4].split(',')]

            for row in range(start[0], end[0] + 1):
                for column in range(start[1], end[1] + 1):

                    if action == 'turn' and command[1] == 'on':
                        if not light_grid[row][column]:
                            light_grid[row][column] = True
                            lights_on += 1

                    elif action == 'turn' and command[1] == 'off':
                        if light_grid[row][column]:
                            light_grid[row][column] = False
                            lights_on -= 1

                    elif action == 'toggle':
                        light_grid[row][column] = not light_grid[row][column]

                        if light_grid[row][column]:
                            lights_on += 1

                        else:
                            lights_on -= 1

    print(lights_on)


def part_two():
    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]

    total_brightness = 0

    with open('2015/day06/input.txt') as file:
        for line in file:
            command = line.split()
            action = command[0]

            if action == 'toggle':
                start = [int(x) for x in command[1].split(',')]
                end = [int(x) for x in command[3].split(',')]
            else:
                start = [int(x) for x in command[2].split(',')]
                end = [int(x) for x in command[4].split(',')]

            for row in range(start[0], end[0] + 1):
                for column in range(start[1], end[1] + 1):

                    if action == 'turn' and command[1] == 'on':
                        # if not light_grid[row][column]:
                        light_grid[row][column] += 1
                        total_brightness += 1

                    elif action == 'turn' and command[1] == 'off':
                        if light_grid[row][column] > 0:
                            light_grid[row][column] -= 1
                            total_brightness -= 1

                    elif action == 'toggle':
                        light_grid[row][column] += 2
                        total_brightness += 2

                        # if light_grid[row][column]:
                        #     lights_on += 1

                        # else:
                        #     lights_on -= 1

    print(total_brightness)


if __name__ == '__main__':
    part_two()
