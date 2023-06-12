import numpy as np

prioritySum = 0
comp1 = []
comp2 = []

values = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


with open('day03.txt') as file:
    for line in file:
        for i in range(len(line)):
            if line[i] != '\n':  
                if i < len(line)//2:
                    comp1.append(line[i])
                else:
                    comp2.append(line[i])

        common = np.intersect1d(comp1, comp2)
        prioritySum += values.index(common[0]) + 1
        comp1 = []
        comp2 = []

print(prioritySum)
    