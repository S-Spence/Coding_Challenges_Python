import unittest
"""
Problem:
Given an array of integers, return the indices of the two numbers that add up to a given target. 
Input: a: an array of integers, n: int (target value).
Return: the indices of the two values.

Step 1: Ask questions: 
                Are all of the integers positive? -> No
                Are there duplicate numbers in the array? -> Yes
                Will there always be a solution available? What to return if no solution? -> No, return none
                Can there be multiple pairs that add to target value? -> No, one solution.
                
Step 2: Write out test cases
            Example 1:  input -> [1, 3, 7, 9 2], 11
                        output -> [3, 4]
            Example 2:  input -> [1, 3, 7, 9, 2], 25
                        output -> null
            Example 3:  input -> [], 10
                        output -> null 
            Example 4: input -> [5], 5
                        output -> null (because you need two numbers that will give that target. This one is important and easy to miss!)
            Example 5:  input -> [1, 6], 7
                        output -> [0, 1]
Step 3: Figure out a solution without code.
                Use a hash table to store a mapping of value-indexes. Search for two values that sum to the number by 
                checking if val-curr is in the dictionary. If so, return the pair, if not, move to the next value in the dict.
Step 4: Check for errors and spell-checks.

"""

def two_sum(nums: "list[int]",target: int ) -> int:
    """Return the two indices whose values sum to the target"""

    # Dictionary to store indices
    index = {}
    # Cannot make a pair with less than 2 elements
    if len(nums) < 2:
        return
    # Add elements and indices to dictionary O(n) space.
    for i in range(len(nums)):
        # Store index values in a list for duplicate elements. Drop duplicates if a 
        # duplicate pair will not sum to the target.
        if nums[i] not in index.keys():
            index[nums[i]] = i
        else:
            if nums[i] + nums[i] == target:
                return [index[nums[i]], i]
                   
        # Find the first matched sum for the target value and return. O(n) time worst case. 
        for val in index.keys():
            if target-val in index.keys() and index[target-val] != index[val]:
                return [index[val], index[target-val]]

    
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.tests = [
            [], 
            [1, 3, 7, 9, 2],
            [1, 3, 7, 9, 2],
            [5],
            [1, 6],
            [3, 3]
            ] 
        self.tests2 = [0, 11, 25, 5, 7, 6]
        self.answers = [None, [3, 4], None, None, [0,1], [0, 1]]
    

    def test_1(self):
        self.assertTrue(two_sum(self.tests[0], self.tests2[0]) == self.answers[0])
    def test_2(self):
        self.assertTrue(two_sum(self.tests[1], self.tests2[1]) == self.answers[1])
    def test_3(self):
        self.assertTrue(two_sum(self.tests[2], self.tests2[2]) == self.answers[2])
    def test_4(self):
        self.assertTrue(two_sum(self.tests[3], self.tests2[3]) == self.answers[3])
    def test_5(self):
        self.assertTrue(two_sum(self.tests[4], self.tests2[4]) == self.answers[4])
    def test_6(self):
        self.assertTrue(two_sum(self.tests[5], self.tests2[5]) == self.answers[5])

# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
