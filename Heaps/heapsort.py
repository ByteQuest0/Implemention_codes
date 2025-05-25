def heapify(arr, n, i):
    # find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    # swap and continue if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    # build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)


# quick test
arr = [12, 11, 13, 5, 6, 7]
print("original:", arr)
heapsort(arr)
print("sorted:", arr)
