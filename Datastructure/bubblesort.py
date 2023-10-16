def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(arr)
        print()
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break


# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90, 5]
print(unsorted_array)
print()

bubble_sort(unsorted_array)
print(unsorted_array)
