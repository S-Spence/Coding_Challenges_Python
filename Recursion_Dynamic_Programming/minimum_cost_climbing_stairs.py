import unittest
"""
Problem: For a given  staircase, the ith step is assigned a non-negative cost indicated by a cost array. 

        Once you pay the cost for a step, you can either climb one or two steps. Find the minimum cost to reach the top
        of he staircase. Your first step can either be the first or second step.

        Leetcode: https://leetcode.com/problems/min-cost-climbing-stairs/  

        Example: 
            Input: cost = [10,15,20]
            Output: 15
            Explanation: You will start at index 1.
                        - Pay 15 and climb two steps to reach the top.
                        The total cost is 15.

Constraints: 
    What if the array is empty? 
    What if there is only one step?


Note: Not all problems that have a dynamic programming solution require that solution. Most of the time, optimization problems 
      based on min/max have an optimal solution that uses dynamic programming.

Solution: You must identify the minimum cost to reach that step. n-1 and n-2 are the only ways to reach step n.
        
        The top-down solution starts at the top step and backtracks, finding the minimum value to each step.
        This approach uses memoization.

        The bottom-up solution builds from the base values up to the solution. This method uses an iterative approach instead of
        recursion. Finding the bottom-up approach is as challenging as looking for the recursive relationship.

        This solution usually offers a space optimzation, such as recognizing that you only need the previous two values for
        this problem. 

"""
"""
Solution 1: Top-down approach
"""
def min_cost(staircase: "list[int]", memo: dict, start: int):
    """
    Recursive function to determine the minimum cost of climbing stairs.
    Note: Without memoization, this function has time: O(2^n), Space: O(n).
    With Memoization: Runtime: O(n), Space: O(n)
    """
    # If the stair is out of bounds, return 0
    if start < 0:
        return 0
    # If it is at the bottom two stairs, return that stair's value
    if start == 0 or start == 1:
        return staircase[start]
    # If the calculation is in the memoization dictionary, return it
    if start in memo:
        return memo[start]
    # Else, add the new min calculation to the memoization dictionary
    memo[start] = staircase[start] + min(min_cost(staircase, memo, start-1), min_cost(staircase, memo, start-2))
    return memo[start]

def min_cost_staircase_td(staircase: "list[int]"):
    """Define a memoized (top down) solution to determine the minimum cost to reach the top of a staircase"""
    # Start at the top of the staircase
    length = len(staircase)
    # Memoization dictionary
    memo = {}
    # call recursive function
    return min(min_cost(staircase, memo, length-1), min_cost(staircase, memo, length-2))

"""
Solution 2: Bottom-up approach. Improves space complexity
"""
def min_cost_staircase_bu(staircase: "list[int]"):
    """
    Bottom-up solution for min cost of climbing stairs.
    Time: O(n), Space: O(1)
    The first solution used a cache for memoization. An optimization was recognizing that the code only uses the previous two
    variables. 
    """
    length = len(staircase)
    # If the length of the stair case is 0, return 0 cost
    if length == 0:
        return 0
    # If the length of the staircase is 1, return the staircase value at 0
    if length == 1:
        return staircase[0]
    # Initialize previous values n-1, n-2
    prev_val = staircase[1]
    prev_prev_val = staircase[0]
    # Iterate through the list and take the minimum value of the previous two stairs and add it to the current value
    for i in range(2, length):
        current = staircase[i] + min(prev_val, prev_prev_val)
        # Update n-1 and n-2
        prev_prev_val = prev_val
        prev_val = current  
    # Return the minimum value at the end
    return min(prev_val, prev_prev_val)


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            [10, 15, 20],
            [1,100,1,1,1,100,1,1,100,1],
            [],
        ]

        self.answers = [15, 6, 0]

    def test_1(self):
        self.assertTrue(min_cost_staircase_td(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(min_cost_staircase_td(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(min_cost_staircase_td(
            self.s[2]) == self.answers[2])
    
    def test_5(self):
        self.assertTrue(min_cost_staircase_bu(
            self.s[0]) == self.answers[0])

    def test_6(self):
        self.assertTrue(min_cost_staircase_bu(
            self.s[1]) == self.answers[1])
    
    def test_7(self):
        self.assertTrue(min_cost_staircase_bu(
            self.s[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
