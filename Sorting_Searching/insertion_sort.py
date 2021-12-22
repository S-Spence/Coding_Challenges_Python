import unittest
"""
Problem: Implement the insertion sort algorithm
        Runtime: O(n^2), Space: O(1)
"""

def insertion_sort(a: "list[int]") -> "list[int]":
    """Implement insertion sort"""
    # Test [5, 1, 3, 4, 2]
    # 1 -> 2 -> 3 -> 4
    for i in range(1, len(a)):
  
        key = a[i] # 1 -> 3 -> 4 -> 2
  
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i-1 # 0 -> 1 -> 2 -> 3
        while j >=0 and key < a[j] :
                a[j+1] = a[j] # a[1] = 5 -> a[2] = 5 -> a[3] = 5 -> a[4] = 5 -> a[3] = 4 -> a[2] = 3
                j -= 1 # -1 -> 0 -> 1 -> 2 -> 1 -> 0
        a[j+1] = key # a[0] = 1 -> a[1] = 3 -> a[2] = 4 -> a[1] = 2
    # [1, 5, 3, 4, 2] -> [1, 3, 5, 4, 2] -> [1, 3, 4, 5, 2] -> [1, 2, 3, 4, 5]
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
        self.assertTrue(insertion_sort(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(insertion_sort(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(insertion_sort(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(insertion_sort(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(insertion_sort(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main()
