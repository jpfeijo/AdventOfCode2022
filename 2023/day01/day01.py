with open('2023/day01/input.txt', 'r') as f:
    isFirst = True
    count = 0

    for line in f:
        first = 0
        last = 0

        for char in line:
            if char.isnumeric():
                if isFirst:
                    first = char
                    last = char
                    isFirst = False

                else:
                    last = char

        isFirst = True
        calibration_value = first + last
        count += int(calibration_value)

    print(count)
