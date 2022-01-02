import unittest
import bst_two_class as bst
import complete_bt as bt
import math
"""
Problem: Validate a binary search tree. Ensure all values to the left are smaller and all values to he right are greater 

Constraints: 
    ASK THIS for BST problems always..can there be duplciate values? -> Yes, but it is not a valid bst if there are duplicates

Tests:

          12                            12
         /  \                          /  \
        7    18                       15  17  = False
       / \   / \
      5   9  16 25  = True 

         10 = true                     15
                                      /  \
                                     12   17
                                    / \   / \
                                   10 16 16   18 = False

Solution: use depth first search helper function that takes lower and upper boundaries for each node.
          time: O(n) for unbalanced tree
          space: O(n) for unbalanced tree because the recursion call stack would be full
"""


def dfs(node, lower_boundary: int, upper_boundary: int) -> bool:
    """
    Helper function to determine if a given node is valid. 
    Time: O(n), if the tree is unbalanced 
    Space: O(n) if entire callstack is full for unbalanced tree.
    """
    # If the node is not within the valid boundaries, return false
    if node.value <= lower_boundary or node.value >= upper_boundary:
        return False

    # If there is a left node, shift boundaries and validate again. The upper boundary for the left side is the node.
    if node.left:
        if dfs(node.left, lower_boundary, node.value) == False:
            return False
    # If there is a right node, shift boundaries and validate again. The lower boundary for the right side is the node.
    if node.right:
        if dfs(node.right, node.value, upper_boundary) == False:
            return False

    return True


def validate_bst(root) -> bool:
    """Determine if a tree is a valid bst"""

    if root == None:
        return True

    return dfs(root, -math.inf, math.inf)


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test_trees = [
            [12, 7, 18, 59, 16, 25],
            [12, 15, 17],
            [10],
            [15, 12, 17, 11, 16, 16, 18]
        ]

        # Initialize trees
        self.tree_1 = bst.BST()
        self.tree_2 = bt.CBT(bt.TreeNode(self.test_trees[1][0]))
        self.tree_3 = bst.BST()
        self.tree_4 = bt.CBT(bt.TreeNode(self.test_trees[3][0]))

        # Fill trees
        for val in self.test_trees[0]:
            self.tree_1.insert(val)

        for i in range(1, len(self.test_trees[1])):
            self.tree_2.insert(self.test_trees[1][i])

        self.tree_3.insert(self.test_trees[2][0])

        for i in range(1, len(self.test_trees[3])):
            self.tree_4.insert(self.test_trees[3][i])

        self.answers = [True, False, True, False]

    def test_1(self):

        self.assertTrue(validate_bst(
            self.tree_1.root) == self.answers[0])

    def test_2(self):

        self.assertTrue(validate_bst(
            self.tree_2.root) == self.answers[1])

    def test_3(self):

        self.assertTrue(validate_bst(
            self.tree_3.root) == self.answers[2])

    def test_4(self):

        self.assertTrue(validate_bst(
            self.tree_4.root) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main()
