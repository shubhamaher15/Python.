#Write a generator function which generates prime numbers up to n.
def generate_primes(n):
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num  
n = int(input("Generate primes up to: "))
print(f"Prime numbers up to {n}:")
for prime in generate_primes(n):
    print(prime, end=" ")
