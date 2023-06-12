floor = 0

with open('2015/input.txt') as file:
    for line in file:
      for character in line:
         if character == "(":
            floor += 1
         elif character == ")":
            floor -= 1
          
print(floor)