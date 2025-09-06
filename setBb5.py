my_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 3, 7)

repeated_items = set()

seen = set()

for item in my_tuple:
    if item in seen:
        repeated_items.add(item)
    else:
        seen.add(item)

print("Repeated items:", repeated_items)
