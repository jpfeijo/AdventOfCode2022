prioritySum = 0
comp1 = []
comp2 = []

with open('day03.txt') as file:
    for line in file:
        for i in range(len(line)):
            if line[i] != '\n':  
                if i < len(line)//2:
                    comp1.append(line[i])
                else:
                    comp2.append(line[i])
        
        comp1 = []
        comp2 = []

    