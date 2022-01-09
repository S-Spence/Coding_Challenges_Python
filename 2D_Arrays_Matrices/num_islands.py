import unittest
from collections import deque
"""
Problem: Given a 2d array containing only 1s which are land and 0s which is water, count the number of islands.
         An island is land that is connected horizontally or vetically.
         Ex:
         [
         [1, 1, 1, 1, 0]
         [1, 1, 0, 1, 0]
         [1, 1, 0, 0, 1]
         [0, 0, 0, 1, 1]
         ]
         output = 2

        Leetcode problem: https://leetcode.com/problems/number-of-islands

Constraints:
        Land cannot be diagonal
        Return 0 if array is empty

Tests: See unit tests below

Solution: Iterate through the matrix in sequential order. Use dfs to solve the subproblem of surrounding islands.
        DFS: Runtime: O(mn), Space: O(mn) -> dfs: Runtime: O(mn), Space: O(max(m,n))
        The bfs version offers a slight spce optimization for added complexity.  
"""

"""
Depth First Search Solution

"""
def search(grid: "list[list[str]]", row: int, col: int):
    """Implement recursive dfs search algorithm"""
    grid[row][col] = "0"

    # Surrounding land to check
    directions = [[row, col-1], [row, col+1], [row-1, col], [row+1, col]]

    for row, col in directions:
        # Check that search is within bounds
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]):
            # If there is another piece of land, call search again
            if grid[row][col] == "1":
                search(grid, row, col)


def num_islands_dfs(grid) -> int:
    """Count the number of islands represented by 1s surrounded on adjacent sides by 0"""
    islands = 0  # count islands

    # Iterate through rows and columns, calling he dfs search function when reaching a 1
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                search(grid, row, col)
                islands += 1
    return islands


"""
Breadth First Search Solution
"""
def num_islands_bfs(matrix: "list[int[str]]"):
    """
    bfs approach to num islands problem
    Time: O(mn), Space: O(max(m,n))
    The bfs solutions offer a small space complexity optimization
    """

    # Return 0 if the matrix is empty
    if len(matrix) == "0":
        return 0

    # Initialize num islands and directions
    num_islands = 0
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # Iterate through the 2D array sequentially
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # If there is land, increment island count, set current spot to zero
            if matrix[row][col] == "1":
                num_islands += 1
                matrix[row][col] = 0
                
                # Initialize queue
                queue = deque()
                queue.append([row, col])

                while len(queue) > 0:
                    curr_pos = queue.popleft()
                    curr_row = curr_pos[0]
                    curr_col = curr_pos[1]
                    # check surrounding land
                    for i in range(len(directions)):
                        curr_dir = directions[i]
                        next_row = curr_row + curr_dir[0]
                        next_col = curr_col + curr_dir[1]
                        # break iteration if it goes out of bounds
                        if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
                            continue
                        # if there is still land, append the next node to queue and set it to 0
                        if matrix[next_row][next_col] == "1":
                            queue.append([next_row, next_col])
                            matrix[next_row][next_col] = "0"
    return num_islands


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.grids = [
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            []

        ]

        self.answers = [1, 3, 0]

    def test_1(self):
        self.assertTrue(num_islands_dfs(
            self.grids[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(num_islands_dfs(
            self.grids[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(num_islands_dfs(
            self.grids[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(num_islands_bfs(
            self.grids[0]) == self.answers[0])

    def test_5(self):
        self.assertTrue(num_islands_bfs(
            self.grids[1]) == self.answers[1])

    def test_6(self):
        self.assertTrue(num_islands_bfs(
            self.grids[2]) == self.answers[2])

# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
