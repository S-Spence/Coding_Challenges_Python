import unittest
"""Leetcode problem: https://leetcode.com/problems/number-of-islands"""


def search(grid: "list[list[str]]", row: int, col: int):
    """Implement recursive dfs search algorithm"""
    grid[row][col] = "0"

    # Surrounding land to check
    surrounding = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]

    for r, c in surrounding:
        # Check that search is within bounds
        if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r]):
            # If there is another piece of land, call search again
            if grid[r][c] == "1":
                search(grid, r, c)


def num_islands(grid) -> int:
    """Count the number of islands represented by 1s surrounded on adjacent sides by 0"""
    islands = 0  # count islands

    # Iterate through rows and columns
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                search(grid, r, c)
                islands += 1
    return islands


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
        self.assertTrue(num_islands(
            self.grids[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(num_islands(
            self.grids[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(num_islands(
            self.grids[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
