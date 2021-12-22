import unittest
"""
Problem: Implment the quick sort algorithm
        Runtime: Best: O(nlogn), worst: O(n^2), Space: O(logn)

        Quicksort shifts elements around in the original array, unlike merge sort that returns a new copy of the array.

"""

def quick_sort(a: "list[int]", left: int, right: int)-> "list[int]":
    """divide and conquer quick sort algorithm"""

    if left < right:
        partition_index = partition(a, left, right)

        quick_sort(a, left, partition_index-1)
        quick_sort(a, partition_index+1, right)
    # Does not need to return a. I just did this to meet the structure of my existing test cases. 
    return a


def partition(a: "list[int]", left: int, right: int) -> int:
    """function to return the partition index to quick sort"""
    pivot = a[right]
    partition_index = left

    for j in range(left, right):
        if a[j] < pivot:
            swap(a, partition_index, j)
            partition_index += 1

    swap(a, partition_index, right)

    return partition_index


def swap(a: "list[int]", index_1, index_2):
    """Helper function to swap elements"""
    temp = a[index_1]
    a[index_1] = a[index_2]
    a[index_2] = temp


print(quick_sort([5, 9, 5, 8, 7, 4, 3, 6, 8], 0, 8))
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
        self.assertTrue(quick_sort(
            self.s[0], 0, len(self.s[0])-1) == self.answers[0])

    def test_2(self):
        self.assertTrue(quick_sort(
            self.s[1], 0, len(self.s[1])-1) == self.answers[1])

    def test_3(self):
        self.assertTrue(quick_sort(
            self.s[2], 0, len(self.s[2])-1) == self.answers[2])

    def test_4(self):
        self.assertTrue(quick_sort(
            self.s[3], 0, len(self.s[3])-1) == self.answers[3])

    def test_5(self):
        self.assertTrue(quick_sort(
            self.s[4], 0, len(self.s[4])-1) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main()
