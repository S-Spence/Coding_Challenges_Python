import unittest
"""
Given an array of positive integers, each integer represents the height of a veticle line on a chart. Find two lines, which together
with the x-axis, form a container that would hold the greatest amount of water.
Return: the area of water it would hold. 

Step 1: Ask questions
    Does the thickness of the line matter? -> No
    Do the left and right sides of the graph count as walls? -> No, the sides cannot be used to form a container.
    Is it safe to assume no negative values in input? -> Yes
Step 2: Strategy, work from both ends of the list to find the greatest area. Two pointer approach. Move the pointer to the smaller
       value at each iteration.
Step 3: Code
Step 4: Test -> inline manual test on brute force solution for interview prep. 

"""
def largest_container(heights: "list[int]") -> int:
    """Viewing the list elements as heights on a bar chart, return the container with the greatest area."""
    """
    max_area = 0
    # No area if less than two lines
    if len(height) < 2:
        return 0
    # [7, 1, 2, 3 9] -> 28
    # Brute force solution O(n^2)
    for i in range((len(height)-1)):
       for j in range(i+1, len(height)):
           distance = j-i # 1, 2, 3, 4 -> 1, 2, 3 -> 1, 2 -> 1
           area = min(height[i], height[j]) * distance # 1, 4, 9, 28 -> 1, 2, 3 -> 2, 4 -> 3

           if area > max_area:
               max_area = area # 1, 4, 9, 28  -> 28, 28, 28 -> 28, 28 -> 28
        
    return max_area
    """

    """Optimizing the brute force solution using two pointers"""
    max_area = 0
    
    # No area with under two elements
    if len(heights) < 2:
        return 0
    # Initialize pointers O(1) space
    p1 = 0
    p2 = len(heights) - 1
    # Loop until the pointers meet. Worst case O(n) time? 
    while(p1 < p2):
        height = min(heights[p1], heights[p2])
        width = p2 - p1
        area = height * width

        max_area = max(max_area, area)

        # Move the pointer to the smaller value
        if heights[p1] <= heights[p2]:
            p1+=1
        else:
            p2-=1

    return max_area


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.tests = [
            [7, 1, 2, 3, 9], 
            [6, 9, 3, 4, 5, 8],
            [1,8,6,2,5,4,8,3,7],
            [1, 1],
            [4,3,2,1,4],
            [1, 2, 1]
            ] 
        self.answers = [28, 32, 49, 1, 16, 2]
    

    def test_1(self):
        self.assertTrue(largest_container(self.tests[0]) == self.answers[0])
    def test_2(self):
        self.assertTrue(largest_container(self.tests[1]) == self.answers[1])
    def test_3(self):
        self.assertTrue(largest_container(self.tests[2]) == self.answers[2])
    def test_4(self):
        self.assertTrue(largest_container(self.tests[3]) == self.answers[3])
    def test_5(self):
        self.assertTrue(largest_container(self.tests[4]) == self.answers[4])
    def test_6(self):
        self.assertTrue(largest_container(self.tests[5]) == self.answers[5])

# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)



