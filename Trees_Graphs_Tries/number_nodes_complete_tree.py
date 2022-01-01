import complete_bt as cbt
import unittest
import math
"""
Problem: Given a complete binary tree, count the number of nodes
         Leetcode: https://leetcode.com/problems/count-complete-tree-nodes/ 

Note: Full Tree: A tree where every tree node has either 0 or 2 chidren.
      Complete Tree: Every level is completely full aside from the last level. If the last level is not full, all node must be as far left as possible. 
      BFS and DFS are both valid to count the nodes along the way. This observation means there is a more optimal solution.
      Focus on the fact that it is a complete binary tree, meaning every level will be full except the last.

Tests:
    input = [7, 8, 9, 10, 11, 12, 13] -> 7
    input = [7, 8, 9, 10] -> 4
    input = [7, 8, 9, 10, 11] -> 5
    input = [1] -> 1

Solution: You can get height in O(logn) and use the formula (2^h-1)-1 to calculate the number of nodes.


"""

"""
Set up and insert for a complete binary tree

"""


def get_height(head: cbt.TreeNode) -> cbt.TreeNode:
    """Return the height of a tree O(logn)"""
    # initialize height to zero. This returns height of 0 when only one node
    height = 0
    # In a complete binary tree, the left side will always have the greatest height.
    while head.left != None:
        height += 1
        head = head.left
    return height


def node_exists(index: int, height: int, node: cbt.TreeNode) -> bool:
    """Determine if a node exists in the tree"""
    # Initialize left and right pointers
    left = 0
    right = math.pow(2, height) - 1
    # loop variable
    count = 0
    # Perform binary search O(logn)
    while count < height:
        middle = (left + right)//2 + 1

        if index >= middle:
            node = node.right
            left = middle
        else:
            node = node.left
            right = middle - 1

        count += 1

    return node != None


def count_nodes(head: cbt.TreeNode) -> int:
    """
    Return a count of the nodes in a complete binary tree in time: O(h^2) where h is the height of the tree or 
    O(logn) * O(logn). 
    Space: O(1)
    """
    if head == None:
        return 0
    # Runs in O(h) or O(logn) where n is the number of potential children in the tree
    height = get_height(head)
    # Return one node if height is zero
    if height == 0:
        return 1
    # Upper count is the max number of nodes on the bottom level
    upper_count = math.pow(2, height) - 1
    # Initialize left and right values for binary search
    left = 0
    right = upper_count
    # Perform binary search. O(logn). You can also say O(h) for height
    while left < right:
        middle = (left + right)//2 + 1
        # determine if the node exists in the right side. O(h) also.
        if node_exists(middle, height, head):
            left = middle
        else:
            right = middle - 1

    return upper_count + left + 1


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test_trees = [
            [7, 8, 9, 10, 11, 12, 13],
            [7, 8, 9, 10],
            [7, 8, 9, 10, 11],
            [1]
        ]

        # Initialize trees
        self.tree_1 = cbt.CBT(cbt.TreeNode(self.test_trees[0][0]))
        self.tree_2 = cbt.CBT(cbt.TreeNode(self.test_trees[1][0]))
        self.tree_3 = cbt.CBT(cbt.TreeNode(self.test_trees[2][0]))
        self.tree_4 = cbt.CBT(cbt.TreeNode(self.test_trees[3][0]))

        self.answers = [7, 4, 5, 1]
        # Fill trees
        for i in range(1, len(self.test_trees[0])):
            self.tree_1.insert(self.test_trees[0][i])

        for i in range(1, len(self.test_trees[1])):
            self.tree_2.insert(self.test_trees[1][i])

        for i in range(1, len(self.test_trees[2])):
            self.tree_3.insert(self.test_trees[2][i])

    def test_1(self):

        self.assertTrue(count_nodes(
            self.tree_1.root) == self.answers[0])

    def test_2(self):

        self.assertTrue(count_nodes(
            self.tree_2.root) == self.answers[1])

    def test_3(self):
        self.assertTrue(count_nodes(
            self.tree_3.root) == self.answers[2])

    def test_4(self):
        self.assertTrue(count_nodes(
            self.tree_4.root) == self.answers[3])

# Run tests
if __name__ == "__main__":
    unittest.main()
