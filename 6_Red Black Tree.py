class Node:
    def __init__(self, key, color, parent=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'BLACK')
        self.root = self.NIL

    def left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def insert(self, key):
        new_node = Node(key, 'RED')
        current = self.root
        parent = None

        while current != self.NIL:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'BLACK'

    def _in_order_traversal(self, node, result):
        if node != self.NIL:
            self._in_order_traversal(node.left, result)
            result.append(str(node.key) + ('(R)' if node.color == 'RED' else '(B)'))
            self._in_order_traversal(node.right, result)

    def display(self):
        result = []
        self._in_order_traversal(self.root, result)
        return " -> ".join(result)


# Example usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    values = [55, 40, 65, 60, 75, 57, 58, 10, 20, 15]

    for val in values:
        rb_tree.insert(val)

    print(rb_tree.display())
