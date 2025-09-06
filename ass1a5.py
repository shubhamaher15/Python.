#Write a Python program to get a string from a given string where all occurrences of its first char 
#have been changed to '$', except the first char itself. Sample String: 'restart'  Expected 
#'resta$t' 
input_string = input("Enter a string: ")

if input_string:
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    print("Modified string:", modified_string)
else:
    print("Empty string entered.")
