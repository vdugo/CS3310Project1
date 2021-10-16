def merge(arr, start, mid, end):
    # Making the left and right copies
    # mergesort is not an in place sorting algorithm
    # so we must use extra space
    L = arr[start:mid + 1]
    R = arr[mid + 1:end + 1]

    # i is to keep track of L, j is to keep track of R
    # and k is to keep track of arr
    i = 0
    j = 0
    k = start
    # loop through both the left subarray and the right subarray
    # until there are no more elements in one or the other
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        
        k += 1
    
    # still need to check if there are leftover elements
    # in either the left subarray or the right subarray
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def mergesort(arr, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    mergesort(arr, start, mid)
    mergesort(arr, mid + 1, end)
    merge(arr, start, mid, end)


