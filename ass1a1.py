#Write a python script which accepts 5 integer values and prints “DUPLICATES” if any of the 
#values entered are duplicates otherwise it prints “ALL UNIQUE”. Example: Let 5 integers are (32, 
#45, 90, 45, 6) then output “DUPLICATES” to be printed. 
numbers = []

print("Enter 5 integers:")
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

if len(numbers) == len(set(numbers)):
    print("ALL UNIQUE")
else:
    print("DUPLICATES")
