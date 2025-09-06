#Define a function that accept two strings as input and find union and intersection of them.
def union_intersection(str1, str2):
   
    set1 = set(str1)
    set2 = set(str2)

    union = set1 | set2          
    intersection = set1 & set2   
    return union, intersection

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

u, i = union_intersection(s1, s2)

print("Union of characters:", u)
print("Intersection of characters:", i)
