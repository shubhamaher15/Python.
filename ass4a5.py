#Write generator function which generate even numbers up to n
def generate_evens(n):
    for i in range(2, n+1, 2):  
        yield i

n = int(input("Enter value of n: "))

print(f"Even numbers up to {n}:")
for num in generate_evens(n):
    print(num, end=" ")
