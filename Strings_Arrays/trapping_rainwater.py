import unittest
"""
   Given an array representing an elevation map where the width of the each bar is 1,
   return how much rainwater can be trapped.
   Leetcode (hard): https://leetcode.com/problems/trapping-rain-water/ 

   This is a bar chart where there are no gaps between bars unless a zero appears.
   If rain fell down on the chart, water could only get trapped where the 0s appear.
   Determine how many unit blocks can be filled with water.
   Step 1: questions..
            can the sides be used to trap water? -> No
            will there be negative inegers? -> No
   
   Ex: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2,1] -> 6
   Step 2: solutions -> 
                    Abstract thinking: This question requires the entire array to generate the solution.
                    Note that the water can never exceed the smaller of the two walls. 
                    Also, no matter where you are, the edge of that container will be the greatest number to the left
                    and the greatest number to the right, with the non-zero values in between subtracted from the area.
                    
     Step 3: Code solution
     Step 4: Test solution -> inline comments in brute force solutions show manual test iterations for interview prep.
     Step 5: Optimize               
                                     
"""

def trapping_water(heights: "list[int]") -> int:
    """
    Brute force solution: double pointer approach. Time complexity: O(n), space complexity O(1). This gap in space and
    tiem complexity indicates the problem can be optimized. 
    
    total_rainwater = 0
    if len(heights) == 0:
        return 0
    # Inline comments tests manually for interview practice -> [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6. 
    for i in range(len(heights)): 
        # Initialize left and right pointers and a value to store the max values to the left and right i. 
        left_p = i # 0 -> 1 -> 0 -> 2 -> 1 -> 0 -> 1 -> 3 -> 2 -> 1 -> 2 -> 1
        right_p = i # 0 -> 1 -> 0 -> 2 -> 1 -> 0 -> 1 -> 3 -> 2 -> 1 -> 2 -> 1
        max_left = 0 # 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3
        max_right = 0 # 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> 2 -> 2 -> 2 -> 1 -> 0
        # Find max value to the left of i
        while left_p >= 0:
            max_left = max(max_left, heights[left_p])
            left_p -= 1

        # find max value to the right of i
        while right_p < len(heights):
            max_right = max(max_right, heights[right_p])
            right_p += 1

        # The water cannot exceed the smaller wall
        height = min(max_left, max_right) # 0 -> 0 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2 -> 2 -> 1 -> 0
        # Subtract the height at the current element from the available water space for this iteration and add total
        current_water = height - heights[i] # 0 -> -1 -> 1 -> -1 -> 1 -> 2 -> 1 -> -1 -> 0 -> 1 -> -1 -> -1
        # Only add water that is greater than 0
        if current_water > 0: 
            total_rainwater += current_water # 0 -> 0 -> 1 -> 1 -> 2 -> 4 -> 5 -> 5 -> 5 -> 6 -> 6 -> 6

    return total_rainwater
    """
    """Optimized solution. Iterate pointers inward for the two-pointer structure. You need to conditionally move the pointers by finding
        some reason to move one pointer over another.
        How to decide which pointer to move? The smaller of the two walls should move because it is the only one that impacts the amount
        of water. The lesser wall will always be on the side of the pointer that is moving. 

        Time complexity: O(n) (only looks at each element once) with two pointer approch. Space Complexity: O(1)
    """
    total_rainwater = 0
    # Return zero if no container can be formed
    if len(heights) == 0:
        return 0
    # Manual test -> [4,2,0,3,2,5] -> 9
    # Initialize pointers and values to store the left and right walls
    p1 = 0 # 0 -> 1 -> 2 -> 3 -> 4
    p2 = len(heights) -1 # 5 -> 5 -> 5 -> 5 -> 5
    max_left = 0 #
    max_right = 0 # 
    
    # Loop until the pointers meet
    while p1 < p2:
        water = 0
        # Move the pointer to the lower wall, move left pointer if they are equal
        if heights[p1] <= heights[p2]: # p1 = 4 -> 2 -> 0 -> 3 -> 2, p2 = 5 -> 5 -> 5 -> 5 -> 5
            max_left = max(max_left, heights[p1]) # 4 -> 4 -> 4 -> 4 -> 4
            water = max_left - heights[p1] # 0 -> 2 -> 4 -> 1 -> 2
            p1 += 1 # 1 -> 2 -> 3 -> 4 -> 5
        else:
            max_right = max(max_right, heights[p2]) 
            water = max_right - heights[p2]
            p2 -= 1
        # Add current water to total water
        total_rainwater += water # 0 -> 2 -> 6 -> 7 -> 9 
    return total_rainwater


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.tests = [
            [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2,1], 
            [4,2,0,3,2,5],
            [],
            [3, 4, 3],
            ] 
        self.answers = [6, 9, 0, 0]
    

    def test_1(self):
        self.assertTrue(trapping_water(self.tests[0]) == self.answers[0])
    def test_2(self):
        self.assertTrue(trapping_water(self.tests[1]) == self.answers[1])
    def test_3(self):
        self.assertTrue(trapping_water(self.tests[2]) == self.answers[2])
    def test_4(self):
        self.assertTrue(trapping_water(self.tests[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
