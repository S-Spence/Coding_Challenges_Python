import unittest
"""
Problem: implement binary search
        Time: O(logn), Space: O(1)
"""

def binary_search(a: "list[int]", val: int) -> int:
    """Use binary search to return the index of a given val"""

    left = 0
    right = len(a)-1

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
    return None


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [1, 2, 3, 4, 5],
            [1],
            [],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ]

        self.val = [3, 1, 9, 42, 8]

        self.answers = [2, 0, None, None, 7]

    def test_1(self):
        self.assertTrue(binary_search(
            self.s[0], self.val[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(binary_search(
            self.s[1], self.val[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(binary_search(
            self.s[2], self.val[2]) == self.answers[2] or self.answers_alt[0])

    def test_4(self):
        self.assertTrue(binary_search(
            self.s[3], self.val[3]) == self.answers[3])
    def test_5(self):
        self.assertTrue(binary_search(
            self.s[4], self.val[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
