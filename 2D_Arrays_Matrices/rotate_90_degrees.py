import unittest
"""
Problem: Rotate a matrix 90 degrees. 

        Leetcode: https://leetcode.com/problems/rotate-image

Constraints: 
    rotate closkwise or counter clockwise? -> Clockwise
    What to return if the matrix cannot be rotated (len 0 or 1)? -> matrix itself

Solution: 
        There are two methods to solving this problem. The first is to rotate the matrix four elements at a time clockwise.
        The second method is transposing the matrix (reversing rows and cols), then reflecting the matrix across the y-axis
        Follow-up: If you need to rotate counter clockwise, reflect the matrix across the x-axis.
        Both solutions must touch every element once. Both solutions use O(1) space.
        The linear algebra methods are simpler to code without error and explain in an interview.
"""


def rotate_90_degrees(matrix: "list[int[int]]"):
    """Rotate a matrix 90 degrees in place"""

    # get the length of the matrix
    n = len(matrix)

    # transpose the matrix first
    for row in range(n):
        for col in range(row+1, n):
            # reverse row and col elements
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # reflect matrix across the y-axis
    for row in range(n):
        p1 = 0
        p2 = len(matrix[0])-1
        while p1 < p2:
            # reverse elements
            matrix[row][p1], matrix[row][p2] = matrix[row][p2], matrix[row][p1]
            # move pointers
            p1 += 1
            p2 -= 1


"""
Follow-up, what if you had to rotate counter clockwise
"""
def rotate_90_counter(matrix: "list[int[int]]"):
    """rotate a matrix 90 degrees counter clockwise"""
    # get length
    n = len(matrix)

    # transpose matrix
    for row in range(n):
        for col in range(row+1, n):
            # reverse row and col elements
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # reflect across the x-axis
    for col in range(len(matrix[0])):
        p1 = 0
        p2 = n-1

        while p1 < p2:
            matrix[p1][col], matrix[p2][col] = matrix[p2][col], matrix[p1][col]
            p1 += 1
            p2 -= 1


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.grids = [
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ],
            [
                [1]
            ],
            [],
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ]
        ]

        self.answers = [[[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]],
                        [[1]],
                        [],
                        # counter clockwise test
                        [[5, 10, 15, 20, 25], [4, 9, 14, 19, 24], [
                            3, 8, 13, 18, 23], [2, 7, 12, 17, 22], [1, 6, 11, 16, 21]]
                        ]

    def test_1(self):
        rotate_90_degrees(self.grids[0])
        self.assertTrue(self.grids[0] == self.answers[0])

    def test_2(self):
        rotate_90_degrees(self.grids[2])
        self.assertTrue(self.grids[1] == self.answers[1])

    def test_3(self):
        rotate_90_degrees(self.grids[2])
        self.assertTrue(self.grids[2] == self.answers[2])

    def test_4(self):
        rotate_90_counter(self.grids[3])
        self.assertTrue(self.grids[3] == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main()
