class HashTable:
    def __init__(self, size=10):
        """
        Initialize the hash table with the specified size.
        Each bucket is an empty list to handle collisions via chaining.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        A simple hash function that computes the hash of the key.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        If the key already exists, update its value.
        """
        index = self._hash(key)
        chain = self.table[index]

        # Check if the key already exists in the chain
        for i, (k, v) in enumerate(chain):
            if k == key:
                # Update the value for the existing key
                chain[i] = (key, value)
                return

        # If the key is not found, append it to the chain
        chain.append((key, value))

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        If the key does not exist, return None.
        """
        index = self._hash(key)
        chain = self.table[index]

        for k, v in chain:
            if k == key:
                return v

        return None  # Key not found

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        Returns True if the key was successfully removed, False otherwise.
        """
        index = self._hash(key)
        chain = self.table[index]

        for i, (k, v) in enumerate(chain):
            if k == key:
                # Remove the key-value pair from the chain
                del chain[i]
                return True

        return False  # Key not found

    def __str__(self):
        """
        Return a string representation of the hash table.
        """
        items = []
        for i, chain in enumerate(self.table):
            items.append(f"Bucket {i}: {chain}")
        return "\n".join(items)




a = HashTable()

a.insert(10, 12)
a.insert(11, 12)
a.insert(15, 12)
a.insert(5, 12)

print(a.__str__())



