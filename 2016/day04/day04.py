def decrypt_letter(letter, room_id):
    if 'a' <= letter <= 'z':
        new_letter = ord(letter) + room_id
        if new_letter > ord('z'):
            new_letter = ord('a')
    elif letter == '-':
        return ' '
    return chr(new_letter)


def second_half(encrypted_room):
    parts = encrypted_room.strip().split('-')

    sector_id, checksum = parts[-1].split('[')

    for part in parts[:-1]:
        char_list = list(part)

        for i in range(len(char_list)):
            new_char = decrypt_letter(char_list[i], int(sector_id))
            char_list[i] = new_char

        new_string = ''.join(char_list)
        print(new_string)




def first_half(encrypted_room):
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
         id_sum += first_half(line)
        second_half(line)

print(id_sum)
