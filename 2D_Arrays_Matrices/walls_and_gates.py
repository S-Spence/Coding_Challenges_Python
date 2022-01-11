from collections import deque
import unittest

"""
Problem: Given a 2D array containing -1s (walls), 0s (gates), and INFs (empty room), Fill each empty room with the number of steps
        to the nearest gate. 

        If it is impossible to reach a gate, leave INF as the value. INF is equal to 2147483647

        Leetcode: https://leetcode.com/problems/walls-and-gates/

Tests: 
    [inf -1  0  inf]       [3 -1 0 1]
    [inf inf inf -1]  -> [2 2 1 -1]
    [inf -1  inf -1]      [ 1 -1 2 -1]
    [0   -1  inf inf]       [ 0 -1 3 4]


Solutions:
        dfs solution exceeds runtime on one leetcode test case
        bfs solution passes all test cases

"""

# iitialize directions and inf as global varibales to use for both solutions
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
inf = 2147483647

"""
Solution 1: dfs
"""
def set_distances(matrix: "list[int[int]]", row: int, col: int, moves: int):
    """Helper function to find the nearest gate using dfs."""   
    # return if the search is out of bounds 
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or moves > matrix[row][col]:
        return
    # increment moves
    matrix[row][col] = moves
    # recursively search in each direction 
    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]
        set_distances(matrix, next_row, next_col, moves + 1)

    
def nearest_gate_dfs(matrix: "list[int[int]]")-> "list[int[int]]":
    """
    Dfs solution to find the set each cell to its distance from the nearest gate
    """
    # return the matrix if it is empty
    if len(matrix) == 0:
        return matrix

    # sequentially update the elements of the matrix to reflect their nearest gate
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                set_distances(matrix, row, col, 0)
    return matrix


"""
Solution 2: bfs 
"""
def nearest_gate_bfs(matrix: "list[int[int]]")->"list[int[int]]":
    """
    bfs solution to finding the nearest gate. This solution passes all leetcode test cases.
    """

    # return 0 if length of matrix is zero
    if len(matrix) == 0:
        return matrix
    # initialize queue and inf
    queue = deque()

    # fill queue with gates
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                queue.append([row, col])

    while len(queue) > 0:
        current = queue.popleft()
        row = current[0]
        col = current[1]

        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]

            # check bounds and empty cell
            if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]) or matrix[next_row][next_col] != inf:
                continue
            # update matrix next value and append the next value to the queue
            matrix[next_row][next_col] = matrix[row][col] + 1
            queue.append([next_row, next_col])

    return matrix


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.grids = [
            [
                [inf, -1, 0, inf],
                [inf, inf, inf, -1],
                [inf, -1, inf, -1],
                [0, -1, inf, inf]
            ],
            [
                [-1]
            ],
            []

        ]

        self.answers = [[[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]], [[-1]], []]

    def test_1(self):
        self.assertTrue(nearest_gate_dfs(
            self.grids[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(nearest_gate_dfs(
            self.grids[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(nearest_gate_dfs(
            self.grids[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(nearest_gate_bfs(
            self.grids[0]) == self.answers[0])

    def test_5(self):
        self.assertTrue(nearest_gate_bfs(
            self.grids[1]) == self.answers[1])

    def test_6(self):
        self.assertTrue(nearest_gate_bfs(
            self.grids[2]) == self.answers[2])

# Run tests
if __name__ == "__main__":
    unittest.main()
