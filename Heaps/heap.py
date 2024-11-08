class MaxHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def parent(self, index):
        # Return the parent index of a given node
        return (index - 1) // 2

    def left_child(self, index):
        # Return the left child index of a given node
        return 2 * index + 1

    def right_child(self, index):
        # Return the right child index of a given node
        return 2 * index + 2

    def insert(self, key):
        """
        Insert a new key into the heap.
        """
        # Add the new key at the end of the heap
        self.heap.append(key)
        # Heapify up to maintain heap property
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        """
        Heapify up process to maintain the max-heap property after insertion.
        """
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            # Swap the current node with its parent
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            # Move up to the parent index
            index = self.parent(index)

    def extract_max(self):
        """
        Remove and return the maximum element from the heap.
        """
        if not self.heap:
            return None  # Heap is empty

        # The maximum element is at the root of the heap
        maximum = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap[-1]
        # Remove the last element
        self.heap.pop()
        # Heapify down to maintain heap property
        self.heapify_down(0)
        return maximum

    def heapify_down(self, index):
        """
        Heapify down process to maintain the max-heap property after deletion.
        """
        size = len(self.heap)
        largest = index

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            # Check if left child exists and is greater than current largest
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            # Check if right child exists and is greater than current largest
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            # If largest is not the current index, swap and continue heapifying
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

    def build_heap(self, array):
        """
        Build a heap from an existing array of elements.
        """
        self.heap = array[:]
        # Start from the last non-leaf node and heapify down each node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def get_max(self):
        """
        Return the maximum element in the heap without removing it.
        """
        if self.heap:
            return self.heap[0]
        return None

    def size(self):
        """
        Return the number of elements in the heap.
        """
        return len(self.heap)

    def is_empty(self):
        """
        Check if the heap is empty.
        """
        return len(self.heap) == 0

    def clear(self):
        """
        Remove all elements from the heap.
        """
        self.heap = []

    def __str__(self):
        """
        String representation of the heap.
        """
        return str(self.heap)


class MinHeap:
    def __init__(self):
        # Initialize an empty list to store heap elements
        self.heap = []

    def parent(self, index):
        # Return the parent index of a given node
        return (index - 1) // 2

    def left_child(self, index):
        # Return the left child index of a given node
        return 2 * index + 1

    def right_child(self, index):
        # Return the right child index of a given node
        return 2 * index + 2

    def insert(self, key):
        """
        Insert a new key into the heap.
        """
        # Add the new key at the end of the heap
        self.heap.append(key)
        # Heapify up to maintain heap property
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        """
        Heapify up process to maintain the min-heap property after insertion.
        """
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            # Swap the current node with its parent
            self.heap[self.parent(index)], self.heap[index] = \
                self.heap[index], self.heap[self.parent(index)]
            # Move up to the parent index
            index = self.parent(index)

    def extract_min(self):
        """
        Remove and return the minimum element from the heap.
        """
        if not self.heap:
            return None  # Heap is empty

        # The minimum element is at the root of the heap
        minimum = self.heap[0]
        # Move the last element to the root
        self.heap[0] = self.heap[-1]
        # Remove the last element
        self.heap.pop()
        # Heapify down to maintain heap property
        self.heapify_down(0)
        return minimum

    def heapify_down(self, index):
        """
        Heapify down process to maintain the min-heap property after deletion.
        """
        size = len(self.heap)
        smallest = index

        while True:
            left = self.left_child(index)
            right = self.right_child(index)

            # Check if left child exists and is less than current smallest
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            # Check if right child exists and is less than current smallest
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            # If smallest is not the current index, swap and continue heapifying
            if smallest != index:
                self.heap[index], self.heap[smallest] = \
                    self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def build_heap(self, array):
        """
        Build a heap from an existing array of elements.
        """
        self.heap = array[:]
        # Start from the last non-leaf node and heapify down each node
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def get_min(self):
        """
        Return the minimum element in the heap without removing it.
        """
        if self.heap:
            return self.heap[0]
        return None

    def size(self):
        """
        Return the number of elements in the heap.
        """
        return len(self.heap)

    def is_empty(self):
        """
        Check if the heap is empty.
        """
        return len(self.heap) == 0

    def clear(self):
        """
        Remove all elements from the heap.
        """
        self.heap = []

    def __str__(self):
        """
        String representation of the heap.
        """
        return str(self.heap)


a = MaxHeap()

a.build_heap([-1,1,5,0,0,4,6,7])

a.insert(43)
a.extract_max()

print(a.heap)


priority_queue = MaxHeap()

priority_queue.insert(8)
priority_queue.insert(2)
priority_queue.insert(5)
priority_queue.insert(12)
priority_queue.insert(1)

priority_queue.extract_max()
priority_queue.extract_max()
priority_queue.extract_max()
priority_queue.extract_max()
priority_queue.extract_max()
