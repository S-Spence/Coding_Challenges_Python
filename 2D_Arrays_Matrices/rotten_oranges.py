import unittest
from collections import deque
"""
Problem: You are given a 2D array containing zeros (empty cell), 1s (oranges), and 2s  (rotten oranges).
        Every minute, all fresh oranges immediately adjacent to rotten oranges are rotten. (all 4 sides)
        How many minutes will pass before all oranges are rotten?

Constraints: 
    What to return if the grid is empty? -> 0
    What do we return if we cannot reach all of the oranges or they cannot all rot? -> -1

Tests:
    [
        [2 1 1 0 0]            [1 1 0 0 0]
        [1 1 1 0 0]            [1 1 0 0 0]   = -1       [] = 0
        [0 1 1 1 1]  = 7       [0 0 0 1 1]  
        [0 1 0 0 1]            [0 1 0 0 1]
    ]
    The comments include a manual test that better walks through the solution

Solution: Scan through the array sequentially and count the oranges, rotting oranges, and rotting orange loacations.
        Use bfs to expand in a ringlike pattern and rot surrounding oranges.

"""


def rotting_oranges(matrix: "list[int[int]]") -> int:
    """
    Return how many miniutes it will take to rot all the oranges.
    Runtime: O(nm), Space: O(nm)
    """

    # return 0 if matrix is empty
    if len(matrix) == 0:
        return 0
    """
        [2 1 1 0 0]
        [1 1 1 0 0]
        [0 1 1 1 1]  = 7
        [0 1 0 0 1]
    """
    # keep track of fresh oranges and rotting oranges
    fresh_oranges = 0
    rotting_oranges = deque()
    # directions for bfs
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # determine the location of rotting oranges and the number of fresh oranges with sequential search
    # [0, 0] -> [0, 1] -> [0, 2] -> [0, 3] -> [0, 4]
    # [1, 0] -> [1, 1] -> [1, 2] -> [1, 3] -> [1, 4]
    # [2, 0] -> [2, 1] -> [2, 2] -> [2, 3] -> [2, 4]
    # [3, 0] -> [3, 1] -> [3, 2] -> [3, 3] -> [3, 4]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # count oranges and find rotten oranges
            if matrix[row][col] == 1:
                fresh_oranges += 1 # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7-> 8 -> 9 -> 10 -> 11
            elif matrix[row][col] == 2:
                rotting_oranges.append([row, col]) # [0, 0]

    # track the current queue size and minutes to rot oranges
    current_queue_size = len(rotting_oranges) # 1
    minutes = 0
    # 0 -> 2 -> 3 -> 2 -> 2 -> 2 -> 2 -> 2 -> 1 -> 1 -> 1
    while len(rotting_oranges) > 0:

        if current_queue_size == 0:
            minutes += 1 # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
            current_queue_size = len(rotting_oranges) # 2 -> 2 -> 2 -> 2 -> 1 -> 1 -> 1

        current_orange = rotting_oranges.popleft() # [0, 0] -> [0, 1] -> [1, 0] -> [0, 2] -> [1, 1]  -> [1, 2]
                                                    # [2, 1] -> [2, 2] -> [3, 1] -> [2, 3] -> [2, 4] -> [3, 4]
        # Current queue size keeps track of bfs cycles as one minute by not counting the length added to the queue
        # from the current cycle, but rather, counting it as one cycle. 
        current_queue_size -= 1 # 0 -> 1 -> 0 -> 1 -> 0 -> 1 -> 0 -> 1 -> 0 -> 0 -> 0 -> 0
        row = current_orange[0] # 0 -> 0 -> 1 -> 0 -> 1 -> 1 -> 2 -> 2 -> 3 -> 2 -> 2 -> 3
        col = current_orange[1] # 0 -> 1 -> 0 -> 2 -> 1 -> 2 -> 1 -> 2 -> 1 -> 3 -> 4 -> 4

        for i in range(len(directions)):
            current_dir = directions[i] # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]
                                        # [-1, 0] -> [0, 1] -> [1, 0] -> [0, -1]

            next_row = row + current_dir[0] # -1 -> 0 -> 1 -> 0
                                            # -1 -> 0 -> 1 -> 0
                                            # 0 -> 1 -> 2 -> 1
                                            # -1 -> 0 -> 1 -> 0
                                            # 0 -> 1 -> 2 -> 1
                                            # 0 -> 1 -> 2 -> 1
                                            # 1 -> 2 -> 3 -> 2
                                            # 1 -> 2 -> 3 -> 2
                                            # 2 -> 3 -> 4 -> 3
                                            # 1 -> 2 -> 3 -> 2
                                            # 1 -> 2 -> 3 -> 2
                                            # 2 -> 3 -> 4 -> 3

            next_col = col + current_dir[1] # 0 -> 1 -> 0 -> -1
                                            # 1 -> 2 -> 1 -> 0
                                            # 0 -> 1 -> 0 -> -1
                                            # 2 -> 3 -> 2 -> 1
                                            # 1 -> 2 -> 1 -> 0
                                            # 2 -> 3 -> 2 -> 1
                                            # 0 -> 2 -> 1 -> 0
                                            # 2 -> 3 -> 2 -> 1
                                            # 1 -> 2 -> 1 -> 0
                                            # 0 -> 4 -> 3 -> 2
                                            # 4 -> 5 -> 4 -> 3
                                            # 4 -> 5 -> 4 -> 3

            # If the search is out of bounds, skip to next iteration
            if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
                continue

            # If there is a fresh orange, rot it and append to rotten queue
            if matrix[next_row][next_col] == 1:
                matrix[next_row][next_col] = 2 # [0, 1] = 2 -> [1, 0] = 2 -> [0, 2] = 2 -> [1, 1] = 2 -> [1, 2] = 2
                                               # [2, 1] = 2 -> [2, 2] = 2 -> [3, 1] = 2 -> [2, 3] = 2 -> [2, 4] = 2
                                               # [3, 4] = 2

                fresh_oranges -= 1 # 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0
                rotting_oranges.append([next_row, next_col]) # [0, 1] -> [[0, 1], [1, 0]]
                                                             #  [[1, 0], [0, 2]] -> [[1, 0], [0, 2], [1, 1]]
                                                             # [[1, 1], [1, 2]]
                                                             # [[1, 2][2, 1]]
                                                             # [[2, 1], [2, 2]]
                                                             # [[2, 2], [3, 1]]
                                                             # [[3, 1], [2, 3]]
                                                             # [[2, 4]]
                                                             # [[3, 4]]
            # Rotting = [[0, 2], [1, 1]] -> [[2, 3]]

    # return -1 if some oranges were unreachable
    if fresh_oranges != 0:
        return -1
    
    return minutes # 7


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.grids = [
            [
                [2, 1, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1]
            ],
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 0, 0, 1]
            ],
            []
        ]

        self.answers = [7, -1, 0]

    def test_1(self):
        self.assertTrue(rotting_oranges(
            self.grids[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(rotting_oranges(
            self.grids[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(rotting_oranges(
            self.grids[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
