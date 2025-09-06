#(both included) and the values are square of keys
def print_square_dict():
    d = {}
    for i in range(1, 21):  
        d[i] = i ** 2
    print("Dictionary of numbers (1–20) and their squares:")
    print(d)
print_square_dict()
