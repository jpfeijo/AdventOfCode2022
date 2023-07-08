# Nice string 
# At least 3 vowels
# At least one letter that appears twice in a row
# Does not contain the strings ab, cd, pq, or xy
# How many strings are nice?

nice_strings = 0

with open('2015/day05/input.txt') as file:
    for line in file:
        
        vowels = 0
        has_double_letter = False
        has_prohibited_string = False
        prev_letter = ''

        for char in line:
            if char in 'aeiou':
                vowels += 1
            
            if char + prev_letter == char + char:
                has_double_letter = True

            if prev_letter + char in ['ab', 'cd', 'pq', 'xy']:
                has_prohibited_string = True

            prev_letter = char

        if vowels >= 3 and has_double_letter and not has_prohibited_string:
            nice_strings += 1

print(nice_strings)