import unittest
"""
Problem: Given an array of intergers sorted in ascending order, return the start and ending index of a given target value. IE [2, 4]
        Runtime should be O(logn).
Constraints:
    Will the list have negaives? -> No
    What to return if the array is empty? -> [-1, -1]
    What to return if target not found? -> [-1, -1]
    
Tests:
    [1, 3, 3, 5, 5, 5, 8, 9], 5 -> [3, 5]
    [], 1 -> [-1, -1]
    [1, 2, 3, 4, 5, 6], 4 -> [3, 3]
    [1, 2, 3, 4, 5, 6], 9 -> [-1, -1]

Solution: 
        Use binary search for O(logn) on sorted array.

Code: Space: O(1), Time: O(logn)
"""


def binary_search(a: "list[int]", left: int, right: int, val: int) -> int:
    """Use binary search to return the index of a given val"""

    while left <= right:
        middle = (left + right)//2
        # If the middle element matches, return it
        if a[middle] == val:
            return middle
        # if the value is in the left side of the list, move right pointer
        elif a[middle] > val:
            right = middle-1
        # If the value is in the right side of the list, move the right pointer
        elif a[middle] < val:
            left = middle + 1
    # If it never found the element, return null
    return -1


def start_end_indices(a: "list[int]", target: int) -> "list[int]":
    """Find the start and ending value of a target value in an array. Space: O(1), Time: O(logn)"""
    # Manual test: [3, 3, 5, 5, 5, 9], 5
    # if array is empty, return [-1, -1]
    if len(a) == 0:
        return [-1, -1]

    # Find any location of the value in the array
    find_val = binary_search(a, 0, len(a)-1, target)  # 2

    # If the target was not found, return [-1, -1]
    if find_val == -1:
        return [-1, -1]

    start = find_val  # 2
    end = find_val   # 2

    # 2
    while start != -1:
        # Use a temp variable so we do not reurn -1 after failing the final search
        temp_1 = start  # 2
        # [3, 3, 5, 5, 5, 9], [3, 3], 5 = -1
        start = binary_search(a, 0, start-1, target)
    # Reassign start to temp
    start = temp_1  # 2

    # 2 -> 4 -> 5
    while end != -1:
        # Another temp variable to prevent returning -1
        temp_2 = end  # 2 -> 4
        # [3, 3, 5, 5, 5, 9], [5, 5, 9], 5 = 4 -> [3, 3, 5, 5, 5, 9], [9], 5 = -1
        end = binary_search(a, end+1, len(a)-1, target)
    # reassign end to temp
    end = temp_2  # 4
    # [2, 4]
    return [start, end]


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [1, 3, 5, 5, 5, 8, 9],
            [],
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 5, 6]
        ]

        self.val = [5, 1, 4, 9]

        self.answers = [[3, 5], [-1, -1], [3, 3], [-1, -1]]

    def test_1(self):
        self.assertTrue(start_end_indices(
            self.s[0], self.val[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(start_end_indices(
            self.s[1], self.val[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(start_end_indices(
            self.s[2], self.val[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(start_end_indices(
            self.s[3], self.val[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
