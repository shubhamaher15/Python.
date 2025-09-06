#Write a Python program to remove the characters which have odd index values of a given string. 
input_string = input("Enter a string: ")
result = input_string[::2]
print("String after removing characters at odd indices:", result)
