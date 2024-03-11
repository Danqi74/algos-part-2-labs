class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def _binary_tree_diameter(tree: BinaryTree) -> int:
    if tree is None:
        return 0, 0
    left_diameter, left_tree_length = _binary_tree_diameter(tree.left)
    right_diameter, right_tree_length = _binary_tree_diameter(tree.right)
    current_node_diameter = left_tree_length + right_tree_length
    length_left = left_tree_length + 1
    length_right = right_tree_length + 1
    return max(left_diameter, right_diameter, current_node_diameter), max(length_left, length_right)


def binary_tree_diameter(tree: BinaryTree) -> int:
    result, _ = _binary_tree_diameter(tree)
    return result
