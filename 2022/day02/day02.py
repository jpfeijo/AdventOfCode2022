# 1 Col      |    2 Col
# A Rock     |    X Rock
# B Paper    |    Y Paper
# C Scissors |    Z Scissors

# Points:
# 1 Rock - 2 Paper - 3 Scissors
# 0 Loose - 3 Draw - 6 Win

#def result(theirInput, myInput):
#    if myInput == theirInput:
#        return 3 + myInput
#    
#    # Winning rock
#    elif myInput == 1 and theirInput == 3:
#        return 7
#    
#    # Winning paper 
#    elif myInput == 2 and theirInput == 1:
#        return 8
#
#    # Winning scissors
#    elif myInput == 3 and theirInput == 2:
#        return 9
#
#    # Loosing rock
#    elif myInput == 1 and theirInput == 2:
#        return 1
#
#    # Loosing paper
#    elif myInput == 2 and theirInput == 3:
#        return 2
#    
#    # Loosing scissors
#    elif myInput == 3 and theirInput == 1:
#        return 3

def shouldAnswer(theirInput, myInput):
    if myInput == 1:
        if theirInput == 1:
            return 3
        if theirInput == 2:
            return 1
        if theirInput == 3:
            return 2

    if myInput == 2:
        if theirInput == 1:
            return 4
        if theirInput == 2:
            return 5
        if theirInput == 3:
            return 6

    if myInput == 3:
        if theirInput == 1:
            return 8
        if theirInput == 2:
            return 9
        if theirInput == 3:
            return 7

myPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

otherPoints = {
    'A': 1,
    'B': 2,
    'C': 3
}

points = 0

with open('day02.txt') as file:
    for line in file:
        points += shouldAnswer(otherPoints[line[0]], myPoints[line[2]])

print(points)

# Second part
# X means you need to loose
# Y means you need to draw
# Z means you need to win

