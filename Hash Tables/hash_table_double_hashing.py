class DoubleHashTable:
    """
    A hash table implementation using open addressing
    with double hashing for collision resolution.
    """

    # A special marker to indicate a deleted slot
    _DELETED = object()

    def __init__(self, size=10, prime=7):
        """
        Initialize the hash table with the specified size.
        We'll store either:
          1) None if the slot is empty
          2) (key, value) if the slot is in use
          3) _DELETED if the slot is deleted
        `prime` is used for the second hash function.
        """
        self.size = size
        self.prime = prime  # Used in second hash
        self.count = 0  # Number of active (key, value) pairs
        self.table = [None] * self.size

    def _hash1(self, key):
        """
        Primary hash function:
        """
        return key % self.size

    def _hash2(self, key):
        """
        Secondary hash function:
        """
        return self.prime - (key % self.prime)

    def _find_slot(self, key, for_insert=False):
        """
        Finds the index where the key should be placed (for insertion)
        or where the key exists (for search/delete).

        If `for_insert` is True, it returns the index to insert a new key.
        If `for_insert` is False, it returns the index where the key is found
        or None if the key does not exist.
        """
        index1 = self._hash1(key)
        index2 = self._hash2(key)

        for i in range(self.size):
            # Double hashing formula
            idx = (index1 + i * index2) % self.size

            if self.table[idx] is None:
                # Slot is empty
                if for_insert:
                    # Return this empty index to insert
                    return idx
                else:
                    # Key not found
                    return None
            elif self.table[idx] is self._DELETED:
                # Slot is marked deleted
                if for_insert:
                    # We can reuse this slot
                    return idx
                # Otherwise, keep searching for a match
            else:
                # Occupied slot
                slot_key, _ = self.table[idx]
                if slot_key == key:
                    # If searching, we found it
                    # If inserting, this is the slot to update
                    return idx
                # else keep probing

        # If we've probed the entire table without returning, table is full or key not found
        return None

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        If the table is full, this will fail or you could implement auto-resizing.
        """
        # Check load factor / resizing if needed (optional)
        idx = self._find_slot(key, for_insert=True)
        if idx is not None:
            # If the slot is currently empty or _DELETED, it's a new insertion
            if (self.table[idx] is None) or (self.table[idx] is self._DELETED):
                self.count += 1

            self.table[idx] = (key, value)
        else:
            # No available slot found -> table is full
            raise Exception("Hash table is full or cannot find a spot via double hashing.")

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        If the key does not exist, return None.
        """
        idx = self._find_slot(key, for_insert=False)
        if idx is not None:
            # idx is a valid slot; verify it's not None or _DELETED
            if self.table[idx] not in (None, self._DELETED):
                _, val = self.table[idx]
                return val
        return None

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        Returns True if the key was successfully removed, False otherwise.
        """
        idx = self._find_slot(key, for_insert=False)
        if idx is not None:
            # If the slot is occupied by the key
            if self.table[idx] not in (None, self._DELETED):
                self.table[idx] = self._DELETED
                self.count -= 1
                return True
        return False

    def __str__(self):
        """
        Return a string representation of the hash table.
        """
        items = []
        for i, slot in enumerate(self.table):
            if slot is None:
                items.append(f"Index {i}: [Empty]")
            elif slot is self._DELETED:
                items.append(f"Index {i}: [Deleted]")
            else:
                k, v = slot
                items.append(f"Index {i}: ({k} -> {v})")
        return "\n".join(items)



b = DoubleHashTable(size=8, prime=5)

b.insert(2, 123)
b.insert(10, 123)
b.insert(18, 123)

print(b.__str__())
