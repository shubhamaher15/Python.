#Write a python script to generate Fibonacci terms using generator function. 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

terms = int(input("Enter number of Fibonacci terms: "))
print("Fibonacci Series:")
for num in fibonacci(terms):
    print(num, end=" ")
