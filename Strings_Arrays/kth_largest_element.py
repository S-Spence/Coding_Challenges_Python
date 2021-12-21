import unittest

"""
Problem: Given an unsorted array, return the kth largest element. 
        It is the kth largest element in sorted order, not the kth distinct element.

Step 1: Constraints
        Can we get an array where k is larger than the array length? -> No

Step 2: Tests  
        [2, 3, 1, 2, 4, 2], k = 4 -> 2
        [5, 3, 1, 6, 4, 2], k = 2 -> 5
        [3], k = 1 -> 3

Step 3: Brute force. Python sort function O(nlogn) using timsort 
        (timsort is a hybrid sorting algorithm derived from merge sort and insertion sort).
        Python sorted() returns a new copy of the list. Python .sort() modifies the existing list. 
        .sort() only work for lists.
        Second solution: Using quicksort, best case: O(nlogn) worst case runtime: O(n^2), space: O(logn)
        Optimal solution: Hoare's quickselect algorithm: best case time O(n), worst case time O(n^2k), space: O(1)

        In this case, the brute force using python's built-in sort was the faster worst case algorithm. However, it did not
        have the best space usage. 
"""

""" Brute force with python's built-in timsort
def kth_largest(a: "list[int]", k: int) -> int:
    
    if len(a) == 0:
            return None
    
    # Call the list method .sort() to sort existing list. Time: O(nlogn), Space: O(n)
    # Test [2, 3, 1, 2, 4, 2], 4 
    a.sort() # [1, 2, 2, 2, 3, 4]

    index = len(a) - k
    
    return a[index]
"""


def quick_sort(a: "list[int]", left: int, right: int)-> "list[int]":
    """divide and conquer quick sort algorithm. Best case O(nlogn) worst case: O(n^2). Space: O(logn)"""

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


""" Second solution uses less space than brute force. 
def kth_largest(a: "list[int]", k: int)-> int:

        if len(a) < 1:
                return None

        index_to_find = len(a)-k

        quick_sort(a, 0, len(a)-1)

        return a[index_to_find]
"""

def quick_select(a: "list[int]", left: int, right: int, index_to_find: int)->int:
        """
        Third approach: Quick Select ->  time: best case O(n) worst case O(n^2) in the event a bad partition choice 
                                        space: O(1) because the call stack gets reduced to tail recursion in this case because
                                        each if-branch has a return. Quick select solves kth smallest. 
                                        Using index_to_find = len(a) - k canges the algorithm to find kth largest.
        """
        if left < right:
                partition_index = partition(a, left, right)
                if partition_index == index_to_find:
                        return a[partition_index]
                elif index_to_find < partition_index:
                        return quick_select(a, left, partition_index-1, index_to_find)
                else:
                        return quick_select(a, partition_index+1, right, index_to_find)


def kth_largest(a: "list[int]", k: int)-> int:
        """See time and space complexity notes in quick_select"""
        # Base case
        if len(a) < 1:
                return None
        # kth largest
        index_to_find = len(a)-k

        quick_select(a, 0, len(a)-1, index_to_find)

        return a[index_to_find]


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [2, 3, 1, 2, 4, 2],
            [5, 3, 1, 6, 4, 2],
            [3],
            [],
        ]
        self.k = [4, 2, 1, 0]

        self.answers = [2, 5, 3, None]

    def test_1(self):
        self.assertTrue(kth_largest(
            self.s[0], self.k[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(kth_largest(
            self.s[1], self.k[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(kth_largest(
            self.s[2], self.k[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(kth_largest(
            self.s[3], self.k[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
