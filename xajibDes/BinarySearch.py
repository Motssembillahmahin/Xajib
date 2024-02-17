def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        mid_value = arr[mid]

        if mid_value == target:

            return mid

        elif mid_value < target:

            low = mid + 1

        else:

            high = mid - 1

    return -1


sorted_list = [int(x) for x in input("Enter a sorted list of numbers (space-separated): ").split()]

target_element = int(input("Enter the target element to search: "))

result = binary_search(sorted_list, target_element)

if result != -1:

    print(f"Element {target_element} found at index {result}")

else:

    print(f"Element {target_element} not found in the list")