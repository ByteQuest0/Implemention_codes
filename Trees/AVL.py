class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rebalance(self, node):

        balance = self.get_balance_factor(node)

        if balance > 1:
            if self.get_balance_factor(node.left) < 0:
                return self.left_right_rotate(node)
            return self.right_rotate(node)

        if balance < -1:
            if self.get_balance_factor(node.right) > 0:
                return self.right_left_rotate(node)
            return self.left_rotate(node)

        return node

    def _insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))


        return self.rebalance(root)

    def _delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                return temp
            elif not root.right:
                temp = root.left
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        return self.rebalance(root)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def left_right_rotate(self, z):
        z.left = self.left_rotate(z.left)
        return self.right_rotate(z)

    def right_left_rotate(self, z):
        z.right = self.right_rotate(z.right)
        return self.left_rotate(z)

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.value, end=" ")
            self._inorder(node.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.value, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.value, end=" ")


tree = AVLTree()

tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(3)
tree.delete(10)

tree.preorder()

