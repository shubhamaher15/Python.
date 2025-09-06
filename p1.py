
my_set = set()
while True:
    print("\nCurrent Set:", my_set)
    print("1. Add element")
    print("2. Remove element")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item = input("Enter element to add: ")
        my_set.add(item)
        print(f"'{item}' added.")
        
    elif choice == '2':
        item = input("Enter element to remove: ")
        if item in my_set:
            my_set.remove(item)
            print(f"'{item}' removed.")
        else:
            print(f"'{item}' not found in the set.")
            
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
