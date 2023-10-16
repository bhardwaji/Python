def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


# Example usage:
unsorted_array = [64, 34, 74, 12, 22, 11, 90]
insertion_sort(unsorted_array)
print(unsorted_array)
