def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted portion
        min_index = i
        # Find the index of the minimum element in the remaining unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
