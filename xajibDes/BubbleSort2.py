def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print("After swapping {} and {}: {}".format(array[j], array[j+1], array))
    return array

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        size = int(file.readline())
        array = [int(line) for line in file.readlines()]
    return array

filename = input("Enter the filename: ")
array = read_array_from_file(filename)
print("Original array:", array)
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)