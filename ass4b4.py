#Write a function which print a dictionary where the keys are numbers between 1 and 20
def print_dict():
    d = {}
    for i in range(1, 21):
        d[i] = i ** 2
    print(d)

print_dict()
