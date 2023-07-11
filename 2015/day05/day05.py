nice_strings = 0

with open('2015/day05/input.txt') as file:
    for line in file:
        has_repeat_pair = False
        has_repeat_with_one_between = False

        for i in range(len(line) - 2):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                has_repeat_pair = True

        for i in range(len(line) - 2):
            if line[i] == line[i+2]:
                has_repeat_with_one_between = True

        if has_repeat_pair and has_repeat_with_one_between:
            nice_strings += 1

print(nice_strings)
