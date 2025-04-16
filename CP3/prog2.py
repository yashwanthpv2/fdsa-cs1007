
class TreeNode:
    def __init__(self, data):
        self.data = data      
        self.left = None     
        self.right = None     
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    def in_order_traversal(self):
        self._in_order_recursive(self.root)
    def _in_order_recursive(self, node):
        if node is not None:
            self._in_order_recursive(node.left)
            print(node.data, end=' ')
            self._in_order_recursive(node.right)
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [7, 4, 9, 1, 6, 8, 10]

    for elem in elements:
        tree.insert(elem)

    print("In-order Traversal:")
    tree.in_order_traversal()
