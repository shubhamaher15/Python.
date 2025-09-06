#Write a program to implement the concept of stack using list 
stack = []

def push(item):
    stack.append(item)
    print(f"{item} pushed to stack.")

def pop():
    if not is_empty():
        return stack.pop()
    else:
        print("Stack is empty. Cannot pop.")

def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("Stack is empty. Nothing to peek.")

def is_empty():
    return len(stack) == 0

def display():
    if not is_empty():
        print("Stack contents:", stack)
    else:
        print("Stack is empty.")


while True:
    print("\nOptions: 1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        item = input("Enter item to push: ")
        push(item)
    elif choice == '2':
        popped = pop()
        if popped is not None:
            print("Popped item:", popped)
    elif choice == '3':
        top = peek()
        if top is not None:
            print("Top of stack:", top)
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
