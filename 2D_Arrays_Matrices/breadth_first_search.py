import unittest
"""
Problem: Implement Breadth First Search for a 2D Array

Notes: BFS should start at a node and traverse all surrounding elements first.
       The idea is to expand around the elements in a ring-like pattern to explore all surrounding elements first. 
       Keep track of the next value to explore in a queue.

Constraints:
        What to return if the array is empty? -> []

Solution: Traverse the graph using a queue to store next up, right, down, left values.
          Explore all surrounding elements for each node before moving on to the next node in the queue.
          Space O(n), time: O(n) where n is the number of values in the matrix.

"""


def matrix_traversal_bfs(matrix: "list[int[int]]"):
    """
    Traverse a matrix using bfs and return the value of arrays.
    Space: O(n), Time: O(n) where n is the values in the matrix
    """
    # Return an empty array if there are no values in the matrix
    if len(matrix) == 0:
        return []

    # Initialize an array of moves for up, right, down, left
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # Initialize a matrix to track seen values in the original matrix
    seen_vals = [[0 for col in range(len(matrix[0]))]
                 for row in range(len(matrix))]

    """
    initialize queue. Mention in an interview that a linked list would be more efficient for a queue. However, the array is
    simpler to do because of the time constraints.
    """
    queue = [[0, 0]]
    values = []

    while len(queue) > 0:

        current_pos = queue.pop(0)
        # Initialize row and column values for current positions
        row = current_pos[0]
        col = current_pos[1]
        # Ensure we are within bounds and have not seen the value before. Use continue to skip current iteration if not.
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen_vals[row][col] == 1:
            continue

        # Update seen values and push value to output array
        seen_vals[row][col] = 1
        values.append(matrix[row][col])

        # Take the top, right, down, and left elements to add to the queue
        for move in directions:
            queue.append([row+move[0], col+move[1]])
    return values


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.matrices = [
            [[1, 2, 3, 4], [5, 6, 7, 8], [
                9, 10, 11, 12], [13, 14, 15, 16]],
            [],
        ]

        self.answers = [[1, 2, 5, 3, 6, 9, 4, 7,
                         10, 13, 8, 11, 14, 12, 15, 16], []]

    def test_1(self):
        self.assertTrue(matrix_traversal_bfs(
            self.matrices[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(matrix_traversal_bfs(
            self.matrices[1]) == self.answers[1])


# Run tests
if __name__ == "__main__":
    unittest.main()
