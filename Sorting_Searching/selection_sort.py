import unittest
"""
Problem: Implement Selection Sort
        Selection sort find the smallest element on each iteration and places it as the next in the list
        Runtime: O(n^2), Space O(1)
"""
def selection_sort(a: "list[int]")-> "list[int]":
    """Implement the selection sort algorithm."""
    
    for i in range(len(a)):
        min_index = i # set i to the minimum for the current iteration
        for j in range(i + 1, len(a)):
            # Keep track of the index of the smallest element on every iteration
            if a[j] < a[min_index]:
                min_index = j
        # Swap the minimum value to the current index on every iteration
        temp = a[i]
        a[i] = a[min_index]
        a[min_index] = temp
    return a


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [1, 5, 3, 4, 2],
            [5, 9, 5, 8, 7, 4, 3, 6, 8],
            [],
            [5],
            [5, 1]
        ]

        self.answers = [[1, 2, 3, 4, 5], [3, 4, 5, 5, 6, 7, 8, 8, 9], [], [5], [1, 5]]

    def test_1(self):
        self.assertTrue(selection_sort(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(selection_sort(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(selection_sort(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(selection_sort(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(selection_sort(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main()

