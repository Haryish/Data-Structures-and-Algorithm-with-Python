class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        return y

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root

            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = self.left_rotate(root.left)

            return root.right_rotate(root) if root.left is None else self.right_rotate(root)

        else:
            if root.right is None:
                return root

            if key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.right_rotate(root.right)
            elif key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)

            return root.left_rotate(root) if root.right is None else self.left_rotate(root)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return

        self.root = self.splay(self.root, key)

        if key < self.root.key:
            new_node = Node(key)
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
            self.root = new_node
        elif key > self.root.key:
            new_node = Node(key)
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
            self.root = new_node

    def display(self):
        def print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node.key))
                if node.left is None and node.right is None:
                    return
                print_tree(node.left, level + 1, "L--- ")
                print_tree(node.right, level + 1, "R--- ")

        print_tree(self.root)


# Example usage:
splay_tree = SplayTree()
splay_tree.insert(10)
splay_tree.insert(5)
splay_tree.insert(15)
splay_tree.insert(2)
splay_tree.insert(8)

splay_tree.display()
