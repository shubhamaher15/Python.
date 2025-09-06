#Write a binary search function which searches an item in a sorted list. The function should return 
#the index of element to be searched in the list. 
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_list[mid]

        if mid_val == target:
            return mid  
        elif mid_val < target:
            low = mid + 1 
        else:
            high = mid - 1  

    return -1  

sorted_list = [11,44,88,99,33,5,7]
target = int(input("Enter the element to search: "))

index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found in the list.")
