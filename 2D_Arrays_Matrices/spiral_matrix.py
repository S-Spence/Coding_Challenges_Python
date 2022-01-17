import unittest
"""
Problem: Given a matrix, print its elements in spiral order starting at 0, 0

    Leetcode: https://leetcode.com/problems/spiral-matrix/

Constraints: What to return if the matrix is empty? -> []
            What to return if only one element? -> that element

Solution: Traverse the matrix in sections of right and down, and left and up since these directions will either add one or
          subtract one. Start the column position at -1 since the row will always clear one of the column elements.
          Rutnime: O(mn), Space: O(1)
"""

def spiral_matrix(matrix: "list[list[int]]")->"list[int]":
    """Print a matrix in spiral order"""
    
    # Return an empty list if the matrix is empty
    if len(matrix) == 0:
        return []

    # Initialize row and col count
    rows, cols = len(matrix), len(matrix[0])
    # start in the positive directions
    direction = 1
    
    """
    Initialize rows and cols. Use -1 because in either direction, right and down, 
    or left and up, the col will need to be one less the length because the other row already traversed it. 
    """
    row, col = 0, -1
    # Initialize output
    output = []

    while rows > 0 and cols > 0:
        # Traverse horizontally
        for _ in range(cols):
            col += direction
            output.append(matrix[row][col])
        # Reduce row count
        rows -= 1
        # Traverse vertically
        for _ in range(rows):
            row += direction
            output.append(matrix[row][col])
        # Reduce col count
        cols -= 1

        # Reverse direction
        direction *= -1

    return output

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1]],
            []
        ]

        self.answers = [[1, 2, 3, 6, 9, 8, 7, 4, 5], [1], []]

    def test_1(self):
        self.assertTrue(spiral_matrix(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(spiral_matrix(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(spiral_matrix(
            self.s[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
            