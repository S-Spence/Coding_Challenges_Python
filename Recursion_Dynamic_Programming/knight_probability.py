import unittest
"""
Problem: On a given n x n chessboard, a knight piece will start at the rth row and cth column. The knight will attempt to make k moves.
        A knight can move in 8 possible ways. Each move will choose one of these eight at random. The knight continues moving until it
        finishes k moves or it moves off the chessboard. Return the probability that the knight is on the chessboard after it finishes 
        moving.

Constraints: How many decimals to round to? -> Don't round

Solution: Top-down approach tracking two additional matrices to represent the previous and next moves.
          Time: O(N^2 * k), Space: O(N^2 * k)
"""
def knight_probability(n: int, k: int, row: int, col: int):
    """Determine the probability of the knight remaining on the chessboard."""
    # Create an array to store the directions a knight can move from any location
    directions = [
                [-2, -1],
                [-2, 1],
                [-1, 2],
                [1, 2],
                [2, 1],
                [2, -1],
                [1, -2],
                [-1, -2]
                ]
    # Initialize matrices to track the previous and next moves
    prev_dp = [[0 for x in range(n)] for y in range(n)]
    next_dp = [[0 for x in range(n)] for y in range(n)]

    prev_dp[row][col] = 1
    
    # Loop for the number of moves the knight must make
    for _ in range(1, k+1):
        # Iterate sequentially
        for row in range(n):
            for col in range(n):
                # Check all directions the knight can move
                for i in range(len(directions)):
                    # Set variables for current direction
                    current_dir = directions[i]
                    prev_row = row + current_dir[0]
                    prev_col = col + current_dir[1]

                    # check bounds
                    if prev_row >= 0 and prev_row < n and prev_col >= 0 and prev_col < n:
                        next_dp[row][col] = next_dp[row][col] + prev_dp[prev_row][prev_col]/8
        prev_dp = next_dp
        # Reset the matrix for next move
        next_dp = [[0 for x in range(n)] for y in range(n)]
    # Calculate the probability that the knight is on the chessboard
    result = 0
    for row in range(n):
        for col in range(n):
            result += prev_dp[row][col]
    
    return result


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.n = [3, 1, 2]
        self.k = [2, 0, 2]
        self.row = [0, 0, 1]
        self.col = [0, 0, 1]

        self.answers = [0.06250, 1.00000, 0.00000]

    def test_1(self):
        self.assertTrue(knight_probability(
            self.n[0], self.k[0], self.row[0], self.col[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(knight_probability(
            self.n[1], self.k[1], self.row[1], self.col[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(knight_probability(
            self.n[2], self.k[2], self.row[2], self.col[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
