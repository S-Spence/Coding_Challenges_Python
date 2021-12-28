import unittest
import BST_Two_Class as BST
"""
Problem: Find the maximum depth of a binary search tree. 
        The maximum depth is the number of nodes along the longest path from root node to leaf node.
        Leetcode (Easy): https://leetcode.com/problems/maximum-depth-of-binary-tree/

Constraints: What to return if the tree is empty? -> 0

Solution: Since we are searching for maximum depth, DFS, do not want to traverse every level or every node. 

Complexity will be O(n) because in the worst case of an unbalanced tree, you will need to traverse every node. 

"""

def max_depth(node: BST.TreeNode) -> int:
    """Return the maximum depth of a binary search tree"""
    # If the node is empty, return 0
    if node == None:
        return 0
    # else take the max of the side that does not hit zero, plus the root node
    depth = 1
    
    return depth + max(max_depth(node.left), max_depth(node.right))
 

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test_trees = [
            [7, 9, 3, 4, 2, 1, 11, 42],
            [],
            [1],
            [34, 56, 7, 1, 3, 8, 10, 4, 5, 9]
        ]

        # Initialize trees
        self.tree_1 = BST.BST()
        self.tree_2 = BST.BST()
        self.tree_3 = BST.BST()
        self.tree_4 = BST.BST()

        self.answers = [4, 0, 1, 6]

    def test_1(self):
        
        for val in self.test_trees[0]:
            self.tree_1.insert(val)

        self.assertTrue(max_depth(
            self.tree_1.root) == self.answers[0])

    def test_2(self):
        
        self.assertTrue(max_depth(
            self.tree_2.root) == self.answers[1])

    def test_3(self):
        self.tree_3.insert(1)
        self.assertTrue(max_depth(
            self.tree_3.root) == self.answers[2])

    def test_4(self):
        for val in self.test_trees[3]:
            self.tree_4.insert(val)
        self.assertTrue(max_depth(
            self.tree_4.root) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
