arr = [1, 2, 3, 4, 5, 6, 7]
target = 7


def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return print(
                target, "found in arr at positon", i - 1
            )  # Return the index of the target element
    return -1


linear_search(arr, target)
