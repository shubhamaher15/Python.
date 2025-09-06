#Write a python script using function to calculate  XY  
def power(x, y):
    return x ** y 

x = int(input("Enter value of X: "))
y = int(input("Enter value of Y: "))

print(f"{x} ^ {y} = {power(x, y)}")
