class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0
    current_node_diameter = length_to_leaf(tree.left) + length_to_leaf(tree.right)
    left_diameter = binary_tree_diameter(tree.left)
    right_diameter = binary_tree_diameter(tree.right)
    return max(left_diameter, right_diameter, current_node_diameter)


def length_to_leaf(tree):
    if tree is None:
        return 0
    return 1 + max(length_to_leaf(tree.right), length_to_leaf(tree.left))
