input_str = input("Enter a String: ")
char_count = {}

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
