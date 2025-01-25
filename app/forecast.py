class Node:
    """Node class for BST elements, containing the node's value and its children."""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    """Binary Search Tree class for efficient sorting and retrieval of financial data."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a new value into the BST."""
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traverse(self):
        """Performs an in-order traversal of the BST and returns a sorted list of values."""
        result = []
        self._inorder_traverse_recursive(self.root, result)
        return result

    def _inorder_traverse_recursive(self, node, result):
        if node:
            self._inorder_traverse_recursive(node.left, result)
            result.append(node.value)
            self._inorder_traverse_recursive(node.right, result)

# Function to process incoming financial data
def process_financial_data(prices):
    bst = BinarySearchTree()
    for price in prices:
        bst.insert(price)
    return bst.inorder_traverse()
