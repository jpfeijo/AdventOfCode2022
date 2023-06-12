wrapping_paper_total = 0

with open('2015/day02/input.txt') as file:
    for line in file:
      dimensions = line.split('x')
      dimensions = [int(value) for value in dimensions]

      lowest_dimension = min(dimensions)

      side_0 = 2*dimensions[0]*dimensions[1]
      side_1 = 2*dimensions[1]*dimensions[2]
      side_2 = 2*dimensions[2]*dimensions[0]

      lowest_dimension = min(side_0, side_1, side_2)

      box_total = side_0 + side_1 + side_2 + lowest_dimension
      wrapping_paper_total += box_total 

print(wrapping_paper_total)