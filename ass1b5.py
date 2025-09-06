#Write a python program to count repeated characters in a string. 
def count_repeated_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    repeated_chars = {char: count for char, count in char_count.items() if count > 1}

    return repeated_chars


input_string = input("Enter a string: ")

result = count_repeated_characters(input_string)

print("Repeated characters and their counts:")
for char, count in result.items():
    print(f"'{char}': {count}")
