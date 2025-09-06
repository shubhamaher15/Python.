#Write python script using package to calculate area and volume of cylinder and cuboids.
import math
def cylinder_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def cuboid_area(l, w, h):
    return 2 * (l*w + w*h + h*l)

def cuboid_volume(l, w, h):
    return l * w * h

print("1. Cylinder")
print("2. Cuboid")
choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    r = float(input("Enter radius of cylinder: "))
    h = float(input("Enter height of cylinder: "))
    print("Cylinder Area:", cylinder_area(r, h))
    print("Cylinder Volume:", cylinder_volume(r, h))

elif choice == 2:
    l = float(input("Enter length of cuboid: "))
    w = float(input("Enter width of cuboid: "))
    h = float(input("Enter height of cuboid: "))
    print("Cuboid Area:", cuboid_area(l, w, h))
    print("Cuboid Volume:", cuboid_volume(l, w, h))

else:
    print("Invalid Choice!")
