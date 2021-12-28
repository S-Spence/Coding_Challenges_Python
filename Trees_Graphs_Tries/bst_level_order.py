import unittest
import bst_two_class as BST
"""
Problem: Given a BST, return an array of arrays containing the level order traversal of the tree at each level.
    Leetcode: https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/164/

Tests:
    [7, 9, 3, 4, 2, 1, 11, 42] -> [[7], [3, 9], [2, 4, 11], [1, 42]]
    [] -> []
    [1] -> [[1]]
    [34, 56, 7, 1, 3, 8, 10, 4, 5, 9] -> [[34], [7, 56], [1, 8], [3, 10], [4, 9], [5]]

Solution: BFS for level order traversal. O(n)

Note: The maximum size of the largest level of a BST is N/2. Queue has a space O(n)
"""


def level_order(root: BST.TreeNode) -> "list[list[int]]":
    """return an array of arrays contaning the level order traversal of a BST. Runtime O(n), Space: O(n)"""
    # If the tree is empty, reurn an empty list
    if root == None:
        return []
    # initialize queue and output list
    queue = []
    output_list = []
    # append the root node to the queue
    queue.append(root)
    # Runtime O(n) becaus the while loops only touch each value once
    # output while loop to traverse tree
    while len(queue) > 0:
        length = len(queue)
        count = 0
        curr_level = []
        # inner while loop to track levels
        while count < length:
            # Remove the first node in the queue and add to current level array
            node = queue.pop(0)
            curr_level.append(node.value)
            # Increment count to track nodes added at the this level
            count += 1
            # Determine if there is a left and right child and add to the queue for the next round
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        # Append the current level list to the output list
        output_list.append(curr_level)
    # Return output list
    return output_list


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

        self.answers = [[[7], [3, 9], [2, 4, 11], [1, 42]], [], [
            [1]], [[34], [7, 56], [1, 8], [3, 10], [4, 9], [5]]]

    def test_1(self):

        for val in self.test_trees[0]:
            self.tree_1.insert(val)

        self.assertTrue(level_order(
            self.tree_1.root) == self.answers[0])

    def test_2(self):

        self.assertTrue(level_order(
            self.tree_2.root) == self.answers[1])

    def test_3(self):
        self.tree_3.insert(1)
        self.assertTrue(level_order(
            self.tree_3.root) == self.answers[2])

    def test_4(self):
        for val in self.test_trees[3]:
            self.tree_4.insert(val)
        self.assertTrue(level_order(
            self.tree_4.root) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
