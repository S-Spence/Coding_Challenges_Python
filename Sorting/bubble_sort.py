import unittest
"""
Problem: Implement Bubble Sort

Time: O(n^2), Space: O(1)
"""

def bubble_sort(a: "list[int]")-> "list[int]":
    """Implement the bubble sort algorithm"""
    for i in range(len(a)):
        for j in range(len(a)-1):
            # swap values if they are not in order
            if a[j] > a [j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
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
        self.assertTrue(bubble_sort(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(bubble_sort(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(bubble_sort(
            self.s[2]) == self.answers[2] or self.answers_alt[0])

    def test_4(self):
        self.assertTrue(bubble_sort(
            self.s[3]) == self.answers[3])
    def test_5(self):
        self.assertTrue(bubble_sort(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

