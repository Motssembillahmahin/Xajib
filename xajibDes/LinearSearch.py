def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


user_input = input("Enter a list of numbers separated by space: ")
my_list = list(map(int, user_input.split()))
target_element = int(input("Enter the target element to search: "))
result = linear_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
