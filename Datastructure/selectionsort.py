unsorted_array = [5, 15, 3, 3, 13, 18, 1]


def selectionsort(unsorted_array):
    for i in range(len(unsorted_array)):
        min_val = min(unsorted_array[i:])
        min_index = unsorted_array.index(min_val, i)
        unsorted_array[i], unsorted_array[min_index] = (
            unsorted_array[min_index],
            unsorted_array[i],
        )
    return print(unsorted_array)


selectionsort(unsorted_array)
