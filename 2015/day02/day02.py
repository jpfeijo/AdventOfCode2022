wrapping_paper_total = 0

dimensions = [2, 3, 4]

with open('2015/day02/input.txt') as file:
    for line in file:
      dimensions = line.split('x')
      dimensions = [int(value) for value in dimensions]

      side_1 = dimensions[0] * dimensions[1]
      side_2 = dimensions[1] * dimensions[2]
      side_3 = dimensions[2] * dimensions[0]

      lowest_dimension = min(side_1, side_2, side_3)

      wrapping_paper_total += (side_1 * 2) + (side_2 * 2) + (side_3 * 2) + lowest_dimension



print(wrapping_paper_total)