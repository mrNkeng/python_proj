import unittest
from app.forecast import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    """Unit tests for verifying the BST implementation."""
    def test_insert_and_traverse(self):
        bst = BinarySearchTree()
        values = [20, 10, 30, 25, 35]
        for value in values:
            bst.insert(value)
        self.assertEqual(bst.inorder_traverse(), sorted(values))

if __name__ == '__main__':
    unittest.main()
