def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    user_input = input("Enter elements of the array separated by spaces: ")

    my_array = list(map(int, user_input.split()))

    bubble_sort(my_array)
    print("Sorted array:", my_array)
