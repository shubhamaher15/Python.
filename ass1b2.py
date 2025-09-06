#Write a Python program to get a single string from two given strings, separated by a space and 
#swap the first two characters of each string. 
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xycabz'
def swap_first_two_chars(str1, str2):
  
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least two characters."

   
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

   
    return new_str1 + new_str2


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


result = swap_first_two_chars(str1, str2)
print("Result:", result)
