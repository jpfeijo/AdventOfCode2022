def is_real_room(encrypted_room):
    parts = encrypted_room.strip().split('-')

    sector_id, checksum = parts[-1].split('[')

    char_counts = {}
    for word in parts[:-1]:
        for char in word:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))

    top_chars = ''.join([char for char, _ in sorted_chars[:5]])

    if top_chars == checksum.rstrip(']'):
        return int(sector_id)
    return 0


id_sum = 0

with open('2016/day04/input.txt') as file:
    for line in file:
        id_sum += is_real_room(line)

print(id_sum)
