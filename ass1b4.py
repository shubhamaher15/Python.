#Write a program to implement the concept of queue using list 
queue = []

def enqueue(item):
    queue.append(item)
    print(f"{item} added to the queue.")

def dequeue():
    if not is_empty():
        removed = queue.pop(0)
        print(f"{removed} removed from the queue.")
        return removed
    else:
        print("Queue is empty. Cannot dequeue.")

def is_empty():
    return len(queue) == 0

def display():
    if is_empty():
        print("Queue is empty.")
    else:
        print("Queue contents:", queue)


while True:
    print("\nOptions: 1.Enqueue  2.Dequeue  3.Display  4.Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        item = input("Enter item to enqueue: ")
        enqueue(item)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
