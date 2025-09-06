#Write a python script to accept decimal number and convert it to binary and octal number using 
#function.
def convert_number(n):
    binary = bin(n)   
    octal = oct(n)    
    return binary, octal

num = int(input("Enter a decimal number: "))
binary, octal = convert_number(num)

print("Binary:", binary)
print("Octal:", octal)
