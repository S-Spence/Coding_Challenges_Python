import unittest
"""
Problem: Implement the merge sort algorithm
        merge sort uses recursion.

Runtime: O(nlogn), Space O(n)

"""

def merge_sort(a: "list[int]") -> "list[int]":
    """Implement the merge sort algorithm. Use <= 1 to handle case of empty list"""
    if len(a) <= 1:
        return a
    # Split the list in half until returning single element lists
    split = len(a)//2
    left_partition = merge_sort(a[:split])
    right_partition = merge_sort(a[split:])
    
    return merge(left_partition, right_partition)


def merge(left: "list[int]", right: "list[int]") -> "list[int]":
    """Helper function to merge sub lists"""
    result = []
    # Start the left and right index at 0
    left_index = 0
    right_index = 0
    # Loop while both indices are in range
    while left_index < len(left) and right_index < len(right):
        # Add elements to results array depending on the larger element
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # Add the remaining element into the array if the split was not even
    return result + left[left_index:] + right[right_index:]


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
        self.assertTrue(merge_sort(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(merge_sort(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(merge_sort(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(merge_sort(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(merge_sort(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main()
