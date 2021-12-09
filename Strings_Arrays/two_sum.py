"""Given an array of integers, return the indices of the two numbers that add up to a given target. 
Input: a: an array of integers, n: int (target value).
Return: the indices of the two values."""

def two_sum(nums: "list[int]",target: int ) -> int:
    """
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
        Step 4: Check for errors and spell-checks. This part is hard when you are not used to checking without IDE. 
    """
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

def tests():

    test_one = []
    test_two = [1, 3, 7, 9, 2] # 11 expected [3,4]
    test_three = [1, 3, 7, 9, 2] # 25 and null
    test_four = [5] # 5 expected null
    test_five = [1, 6] # 7 expected [0, 1]
    test_six = [3, 3] # target 6, expected [0, 1]
    

    assert(two_sum(test_one, 0) == None)
    assert(two_sum(test_two, 11) == [3,4])
    assert(two_sum(test_three, 25) == None)
    assert(two_sum(test_four, 5) == None)
    assert(two_sum(test_five, 7) == [0, 1])
    assert(two_sum(test_six, 6) == [0, 1])

    print("Tests passed.")

    """Final solution: O(n) space and O(n) time."""
    """The brute force solution would be O(n^2) time and O(1) space"""

if __name__ == "__main__":
    tests()
