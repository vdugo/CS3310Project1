def partition(arr, start, end):
    partitionIndex = start - 1
    # we choose the pivot to be the last element
    pivot = arr[end]
    
    for index in range(start, end):
        # move the elements less than the pivot to the left of it
        # and the elements greater than the pivot to the right of it
        # quicksort is an in place sorting algorithm,
        # so we don't need to use extra space
        if arr[index] <= pivot:
            partitionIndex += 1
            arr[index], arr[partitionIndex] = arr[partitionIndex], arr[index]
    # last step is to swap the pivot and element at partitionIndex
    arr[partitionIndex + 1], arr[end] = arr[end], arr[partitionIndex + 1]
    return partitionIndex + 1

def quicksort(arr, start, end):
    if len(arr) == 1:
        return
    if start < end:
        partitionIndex = partition(arr, start, end)
        quicksort(arr, start, partitionIndex - 1)
        quicksort(arr, partitionIndex + 1, end)
