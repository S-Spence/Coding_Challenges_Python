import unittest
"""
Problem: Given and mXn integer matrix, if an element is zero, set its entire row and column to zeros and return the matrix. 
        You must do this in place.

Constraints: 
      What to return if the matrix is empty? -> []
Tests: 
    [1, 1, 1]      [1, 0, 1]                   [0, 1, 2, 0]    [0, 0, 0, 0]
    [1, 0, 1]   =  [0, 0, 0]      [] = []      [3, 4, 5, 2] =  [0, 4, 5, 0]
    [1, 1, 1]      [1, 0, 1]                   [1, 3, 1, 5]    [0, 3, 1, 0]
    
Solution: Loop through and track a list of the rows and columns that contain a zero. This runs in O(mn). 
          Loop through the lists of rows and columns and update each element to zero. This is O(mn) + O(mn)
          Overal runtime: O(mn) pace: O(m + n)

"""


def set_zeros(matrix: "list[list[int]]") -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # extra space O(m + n)
    # stores the rows and cols that contain zeros
    rows = []
    cols = []
    # find all zeros rows and cols
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows.append(row)
                cols.append(col)

    # set rows with a zero to all zeros O(mn)
    for row in rows:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0
    # set cols with a zero to all zeros. O(mn)
    for col in cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.grids = [
            [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            [
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5]
            ],
            []
        ]

        self.answers = [[[1, 0, 1], [0, 0, 0], [1, 0, 1]],
                        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], []]

    def test_1(self):
        set_zeros(self.grids[0])
        self.assertTrue(
            self.grids[0] == self.answers[0])

    def test_2(self):
        set_zeros(self.grids[1])
        self.assertTrue(
            self.grids[1] == self.answers[1])

    def test_3(self):
        set_zeros(self.grids[2])
        self.assertTrue(
            self.grids[2] == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
