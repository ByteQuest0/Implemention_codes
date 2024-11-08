def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps were made in this pass
        swapped = False
        # Perform a pass through the array
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Set flag to True indicating a swap was made
                swapped = True
        # If no swaps were made, the list is sorted
        if not swapped:
            break
