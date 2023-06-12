biggestSum = 0
aux = 0
topThree = []

with open('input.txt') as file:
    for line in file:
        if line == '\n':
            if biggestSum < aux:
                biggestSum = aux
                topThree.append(biggestSum)

            aux = 0
            #aux += line
        else:
            aux += int(line)

totalThree = topThree[-1] + topThree[-2] + topThree[-3]


print(totalThree)