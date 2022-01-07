import unittest
"""
Problem: Implement Depth First Search for a 2D Array

Constraints:
        What to return if the array is empty? -> []

Solution: Traverse the graph recursively in the order up, right, down, left. Space O(n), time: O(n) where n is the number of values
          in the matrix.

"""


def dfs(matrix: "list[int[int]]", row: int, col: int, seen_vals: "list[int[int]]", vals: "list[int]"):
    """Recursive function for dfs of a matrix. Track seen values."""
    # Set up moves for up, right, down, left dfs traversal
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # Base case, return if out of bounds or already explored
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen_vals[row][col] == 1:
        return
    # Append the value to the output list and update seen values
    vals.append(matrix[row][col])
    seen_vals[row][col] = 1

    for i in range(len(directions)):
        # Set the current direction
        curr_dir = directions[i]
        # Call dfs to recurse in the current directions
        dfs(matrix, row+curr_dir[0], col+curr_dir[1], seen_vals, vals)


def matrix_traversal_dfs(matrix: "list[int[int]]"):
    """
    Traverse a matrix using dfs and return the value of arrays.
    Space: O(n), Time: O(n), where n represents the elements in the matrix
    """
    # Mirror the matrix in zeros to track seen values
    seen_vals = [[0 for col in range(len(matrix[0]))]
                 for row in range(len(matrix))]
    print(seen_vals)

    values = []

    dfs(matrix, 0, 0, seen_vals, values)

    return values


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.matrices = [
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
                11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
            [],
        ]

        self.answers = [[1, 2, 3, 4, 5, 10, 15, 20, 19,
                         14, 9, 8, 13, 18, 17, 12, 7, 6, 11, 16], []]

    def test_1(self):
        self.assertTrue(matrix_traversal_dfs(
            self.matrices[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(matrix_traversal_dfs(
            self.matrices[1]) == self.answers[1])


# Run tests
if __name__ == "__main__":
    unittest.main()
