import random
import unittest
"""
Problem: Given an array of integers and a value r, could the triplets appearing in progressing order of multiples of r. 

Constraints:
        What to return if the array is empty? -> 0
Tests: 
    # [1, 5, 5, 25, 125], r= 5 -> 4
    # [1, 3, 9, 9, 27, 81] r=3, -> 6
    # [], r= 1 -> 0

Solution: Keep track of two dictionaries. Runtime: O(n), Space: O(n)
"""

def count_triplets(arr: "list[int]", r: int):
    """Count triplets appearing in progressing order in multiples of r"""
    count = 0
    before = dict()
    after = dict()
    
    # Add all elements to the after dictionary
    for val in arr:
        if val in after.keys():
            after[val] += 1
        else: 
            after[val] = 1
    
    """ Iterate through the array, removing the current element from the after list.
        Increase the count if the current value is divisble by r, the current value
        divided by r is in the before dictionary, and the current value multiplied by r is
        in the after dictionary. Finally, move the current element to before dictionary. """
    for val in arr:
        # Remove the element from the after dictionary
        after[val] -= 1
        # If val is divisible by r, val//r in before dict, and val*r in after dict,
        # increase count by the number of matching elements in the before dict * the
        # number of matching elements in the after dict. 
        if val %r == 0 and val//r in before.keys() and val * r in after.keys():
            count += before[val//r] * after[val*r]
        
        # Move the current element to the before dictionary
        if val in before.keys():
            before[val] += 1
        else:
            before[val] = 1  
    
    return count


class TestMethods(unittest.TestCase):
    def setUp(self):
        # Generate some test data
        self.lists = [[1, 5, 5, 25, 125], [1, 3, 9, 9, 27, 81], [1 for i in range(100)], []]
        self.r = [5, 3, 1, 1]
        self.answers = [4, 6, 161700, 0]

    def test_1(self):
        self.assertTrue(count_triplets(
            self.lists[0], self.r[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(count_triplets(
            self.lists[1], self.r[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(count_triplets(
            self.lists[2], self.r[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(count_triplets(
            self.lists[3], self.r[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main()                                         
