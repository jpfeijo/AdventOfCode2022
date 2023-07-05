wrapping_paper_total = 0

with open('2015/day02/input.txt') as file:
    for line in file:
      dimensions = line.split('x')
      dimensions = [int(value) for value in dimensions]

      bow_ribbon = dimensions[0] * dimensions[1] * dimensions[2]

      lowest_dimensions = dimensions[:]
      lowest_dimensions.remove(max(lowest_dimensions))

      wrapping_paper_total += (2 * lowest_dimensions[0]) + (2 * lowest_dimensions[1])
      wrapping_paper_total += bow_ribbon


print(wrapping_paper_total)