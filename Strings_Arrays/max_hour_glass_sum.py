import unittest
"""
Problem: Max Hourglass Sum Challenge
Description: This challenge takes input for a 2D (6X6) array and calculates the sum of all hourglass formations within the array.
             The function then returns the maximum hour glass sum within the array.      

             Hackerrank:  https://www.hackerrank.com/challenges/30-2d-arrays/problem?h_r=profile  

Constraints: Will it always be 6X6? -> Yes

"""


def sum_hour_glass(arr: list) -> int:
    """ Find the sum of the hour glass formation in a 6X6 grid."""
    max_sum = -63   # Store lowest int (-9 * 7) as max int
    
    # Add hourglass values, staying in the range of a 6X6 2d array
    for i in range(4):
        for j in range(4):
            sum_hr = (arr[i][j] + arr[i][j+1] + arr[i][j + 2] + arr[i + 1][j+1] +
                     arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
            # If hour glass sum is greater than max_sum, assign to max_sum
            if sum_hr > max_sum:
                max_sum = sum_hr
                                  
    return max_sum

class TestMethods(unittest.TestCase):
    def setUp(self):
        # Generate some test data
        self.lists = [
            [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
            [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]
            ]
        
        self.answers = [7, 19]

    def test_1(self):
        self.assertTrue(sum_hour_glass(
            self.lists[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(sum_hour_glass(
            self.lists[1]) == self.answers[1])


# Run tests
if __name__ == "__main__":
    unittest.main() 
