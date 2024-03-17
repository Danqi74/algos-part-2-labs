import unittest

from scr.tree_diameter import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(unittest.TestCase):
    def test_binary_tree_diameter_case1(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(8)
        root.left.right.right.left = BinaryTree(5)
        root.left.right.right.left.right = BinaryTree(9)
        root.left.right.right.left.right.right = BinaryTree(6)
        self.assertEqual(binary_tree_diameter(root), 7)

    def test_binary_tree_diameter_case2(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.right = BinaryTree(6)
        root.left.left.left = BinaryTree(7)
        root.left.left.right = BinaryTree(8)
        root.right.right.left = BinaryTree(9)
        root.left.left.left.left = BinaryTree(10)
        root.left.left.left.right = BinaryTree(11)
        root.right.right.left.right = BinaryTree(12)
        self.assertEqual(binary_tree_diameter(root), 8)

    def test_binary_tree_diameter_case3(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        self.assertEqual(binary_tree_diameter(root), 2)

    def test_binary_tree_diameter_with_none(self):
        self.assertEqual(binary_tree_diameter(None), 0)
    
    def test_binary_tree_diameter_new_case(self):
        root = BinaryTree(100)
        root.right = BinaryTree(120)
        root.right.left = BinaryTree(105)
        root.right.right = BinaryTree(125)
        root.left = BinaryTree(50)
        root.left.right = BinaryTree(71)
        root.left.left = BinaryTree(10)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(6)
        root.left.left.left.left.left = BinaryTree(5)
        root.left.left.right = BinaryTree(12)
        root.left.left.right.right = BinaryTree(15)
        root.left.left.right.right.right = BinaryTree(18)
        root.left.left.right.right.right.left = BinaryTree(19)
        root.left.left.right.right.right.left.left = BinaryTree(20)
        self.assertEqual(binary_tree_diameter(root),9)


if __name__ == "__main__":
    unittest.main()
