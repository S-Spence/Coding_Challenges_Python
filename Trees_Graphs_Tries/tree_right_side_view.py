import unittest
import bst_two_class as BST
"""
Problem: Given a binary tree, imagine you are standing on the right side of the tree. Return an array of the values of nodes
        you can see ordered from top to bottom. 

Constraints: What to return if tree is empty? -> []
             Single value tree? ex. 1 -> [1]
             Return the array in top down order
            

Solution: return only the right side of the tree's outter nodes and the other nodes that exceeds its length.
        DFS and BFS can both solve this problem. 

        Solution 1: Use BFS and return the tail value of the queue at each level
        Solution 2: Use DFS, modify pre-order to prioritize right side. Modify base case to only add to list if the
                    level has not been explored. 

        Both solutions have time: O(n), space: O(n)

Note: BFS solution is beter in the event of a skewed tree. DFS is better is event of full and complete tree.  
      Technically space in worst case is O(h) in DFS where h is height of tree. Space in worst case BFS is O(w) where w is the width
      of the tree.

"""


def right_side_view_bfs(root: BST.TreeNode) -> "list[int]":
    """
    Use BFS to determine the right side of view of the tree and return it top-down in array. This will track the nodes at
    each level and return the right most valu at that level.

    """
    # check for empty tree
    if root == None:
        return []
    # define queue and output list
    queue = [root]
    output = []

    # Add the root node to the tree
    while len(queue) > 0:
        # initialize count and length
        length = len(queue)
        count = 0

        while count < length:

            node = queue.pop(0)
            # Only add the value to the output list if it is the right-most node at this level
            if count == length-1:
                output.append(node.value)
            # increase count
            count += 1

            # Enqueue children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return output


def right_side_view_dfs(root: BST.TreeNode) -> "list[int]":
    """
    DFS to find the right-side view of a tree.

    """
    # Initialize output list, depth_right, and depth_left
    output = []
    # Call helper function to track level
    _dfs(root, 0, output)
    # Return the modified output array
    return output


def _dfs(root: BST.TreeNode, level: int, result: "list[int]") -> "list[int]":
    """Private dfs helper function for dfs solution. Worst case time: O(n), space: O(n)"""
    # Return an empty list if the tree is null
    if root == None:
        return []
    # Only add to the output is the level has not been explored. The rightmost element is explored first
    if level >= len(result):
        result.append(root.value)

    # Call recursively on right side and increment current level
    if root.right:
        _dfs(root.right, level+1, result)
    # Call recursively on left and increment current level
    if root.left:
        _dfs(root.left, level+1, result)

    return result


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

        # Fill trees
        for val in self.test_trees[0]:
            self.tree_1.insert(val)
        for val in self.test_trees[3]:
            self.tree_4.insert(val)
        self.tree_3.insert(1)

        self.answers = [[7, 9, 11, 42], [], [1], [34, 56, 8, 10, 9, 5]]

    def test_1(self):

        self.assertTrue(right_side_view_bfs(
            self.tree_1.root) == self.answers[0])

    def test_2(self):

        self.assertTrue(right_side_view_bfs(
            self.tree_2.root) == self.answers[1])

    def test_3(self):

        self.assertTrue(right_side_view_bfs(
            self.tree_3.root) == self.answers[2])

    def test_4(self):

        self.assertTrue(right_side_view_bfs(
            self.tree_4.root) == self.answers[3])

    def test_5(self):

        self.assertTrue(right_side_view_dfs(
            self.tree_1.root) == self.answers[0])

    def test_6(self):

        self.assertTrue(right_side_view_dfs(
            self.tree_2.root) == self.answers[1])

    def test_7(self):

        self.assertTrue(right_side_view_dfs(
            self.tree_3.root) == self.answers[2])

    def test_8(self):

        self.assertTrue(right_side_view_dfs(
            self.tree_4.root) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
