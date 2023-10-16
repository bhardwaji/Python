def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # Choose a pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Example usage:
unsorted_array = [1, 2, 3, 4, 5, 6, 12, 5545, 23, 23, 1, 3, 23, 56, 7, 60]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)
