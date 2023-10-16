arr = [1, 2, 3, 4, 5, 6, 7]
target = 5


def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        pos = left + (right - left) * (target - arr[left]) // (arr[right] - arr[left])
        if arr[pos] == target:
            return pos  # Return the index of the target element
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return -1  # Return -1 if the target is not found


interpolation_search(arr, target)
