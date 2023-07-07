import hashlib

def find_lowest_number(secret_key):
    number = 1
    while True:
        string = secret_key + str(number)
        hash_value = hashlib.md5(string.encode()).hexdigest()
        if hash_value.startswith("00000"):
            return number
        number += 1

secret_key = "iwrupvqb"
lowest_number = find_lowest_number(secret_key)
print(lowest_number)