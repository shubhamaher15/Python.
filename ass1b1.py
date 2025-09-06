#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#If the string length is less than 2, return instead of the empty string. 
#Sample String : 'General12' 
#Expected Result : 'Ge12' 
#Sample String : 'Ka' 
#Expected Result : 'KaKa' 
#Sample String : ' K'
def swap_first_two_chars(str1, str2):
  
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least two characters."
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]

    
    return new_str1 + ' ' + new_str2


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


result = swap_first_two_chars(str1, str2)
print("Result:", result)
