class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False  # Key not found
        if node.val == key:
            return True  # Key found
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def search_iterative(self, key):
        current = self.root
        while current is not None:
            if key == current.val:
                return True
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, node , key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete_node(node.left, key)
        elif key > node.val:
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._min_value_node(node.right)
            node.val = min_larger_node.val
            node.right = self._delete_node(node.right, min_larger_node.val)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=" ")
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)
        print()  # for a newline after traversal

    def _preorder(self, node):
        if node:
            print(node.val, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()  # for a newline after traversal

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=" ")

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None:
            return 0
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return max(left_height, right_height) + 1

    def insert_iterative(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = Node(key)
                    break
                else:
                    current = current.left
            elif key > current.val:
                if current.right is None:
                    current.right = Node(key)
                    break
                else:
                    current = current.right
            else:
                break

    def delete_iterative(self, key):
        current = self.root
        parent = None

        # Step 1: Find the node to be deleted and its parent
        while current and current.val != key:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right

        # If the node wasn't found, return as there's nothing to delete
        if current is None:
            return

        # Step 2: If the node has no children (leaf node)
        if current.left is None and current.right is None:
            if current == self.root:  # If the root is the node to be deleted
                self.root = None
            elif current == parent.left:
                parent.left = None
            else:
                parent.right = None

        # Step 3: If the node has one child
        elif current.left is None:  # Only right child
            if current == self.root:
                self.root = current.right
            elif current == parent.left:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:  # Only left child
            if current == self.root:
                self.root = current.left
            elif current == parent.left:
                parent.left = current.left
            else:
                parent.right = current.left

        # Step 4: If the node has two children
        else:
            # Find the minimum node in the right subtree (in-order successor)
            successor = self._min_value_node(current.right)
            successor_val = successor.val

            # Delete the successor recursively (it will have at most one child)
            self.delete(successor.val)

            # Replace current node's value with the successor's value
            current.val = successor_val



bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)
bst.insert(1)
bst.insert(4)
bst.insert(13)
bst.insert(17)
bst.insert(20)

bst.preorder()
bst.inorder()
bst.postorder()
