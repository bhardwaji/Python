def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the input array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    # return merge(left_half, right_half)
    return print(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result


# Example usage:
unsorted_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)
