class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color  # red or black
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None, color="black")  # Sentinel NIL node
        self.root = self.NIL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, data):
        new_node = Node(data=data)
        new_node.left = new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, z):
        # Case: Parent is red, needing adjustment
        while z.parent and z.parent.color == "red":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Uncle node
                if y.color == "red":
                    # Case 2: Both parent and uncle are red
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent  # Recurse upward
                else:
                    # Case 3: Parent is red, uncle is black, and z is a right child
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)  # Left-rotate to correct shape
                    # Case 3: Left-rotation done, recolor and rotate
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.rotate_right(z.parent.parent)  # Right-rotate to fix violation
            else:
                # Symmetric cases for when z's parent is the right child
                y = z.parent.parent.left
                if y.color == "red":
                    # Case 2: Parent and uncle are both red
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    # Case 3: Parent is red, uncle is black, and z is a left child
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    # Case 3: Recoloring and left-rotation
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.rotate_left(z.parent.parent)
        # Case 1: Root is always black after insertion fix
        self.root.color = "black"

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, data):
        z = self.search(self.root, data)
        if z == self.NIL:
            print("Value not found in the tree.")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "black":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right  # Sibling node
                if w.color == "red":
                    # Case 1: Sibling is red
                    w.color = "black"
                    x.parent.color = "red"
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":
                    # Case 2: Sibling and its children are black
                    w.color = "red"
                    x = x.parent  # Move up the tree
                else:
                    if w.right.color == "black":
                        # Case 3: Sibling is black, left child is red, right is black
                        w.left.color = "black"
                        w.color = "red"
                        self.rotate_right(w)
                        w = x.parent.right
                    # Case 3: Right child of sibling is red
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                # Symmetric cases for when x is the right child
                w = x.parent.left
                if w.color == "red":
                    # Case 1: Sibling is red
                    w.color = "black"
                    x.parent.color = "red"
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == "black" and w.left.color == "black":
                    # Case 2: Sibling and its children are black
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":
                        # Case 3: Sibling is black, right child is red, left is black
                        w.right.color = "black"
                        w.color = "red"
                        self.rotate_left(w)
                        w = x.parent.left
                    # Case 3: Left child of sibling is red
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.rotate_right(x.parent)
                    x = self.root
        # Ensure the final node is black
        x.color = "black"

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def inorder(self):
        self._inorder(self.root)
        print("\n")

    def _inorder(self, node):
        if node != self.NIL:
            self._inorder(node.left)
            print(f"{node.data} ({node.color})", end=" ")
            self._inorder(node.right)


    def preorder(self):
        self._preorder(self.root)
        print("\n")

    def _preorder(self, node):
        if node != self.NIL:
            print(f"{node.data} ({node.color})", end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node != self.NIL:
            self._postorder(node.left)
            self._postorder(node.right)
            print(f"{node.data} ({node.color})", end=" ")


# Example usage
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(5)
rbt.insert(15)
rbt.insert(3)

rbt.insert(2)
rbt.insert(4)
rbt.insert(20)
rbt.insert(16)

rbt.preorder()

rbt.delete(2)

rbt.preorder()


rbt.delete(4)

rbt.preorder()
