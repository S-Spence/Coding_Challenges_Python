import unittest
"""
Problem: Given a queue of people with numbers 1 to n, each person may bribe up to two people directly infront of them in line.
         Determine the number of swaps that took place to get the queue in its given order. If any person made more than two swaps,
         reurn -1.
Constraints: What if the array is empty? -> 0
"""
import random

# Complete the minimumBribes function below.
def minimum_bribes(q: "list[int]"):
    """Given a line where the number represents a person's place, determine the minimum number of bribes that took place."""
    total_bribes = 0     # Create a variable for total bribes

    # iterate backwards
    for i in range(len(q)-1, 0, -1):
        index = i + 1 # index for line starts at one
        
        if q[i] != index:
            # If i made one swap
            if i-1 >= 0 and index == q[i-1]:
                temp = q[i-1]
                q[i-1] = q[i]
                q[i] = temp
                total_bribes += 1
            # If i made two swaps
            elif  i - 2 >= 0 and index == q[i-2]:
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = q[i-2]        
                total_bribes += 2
            else:
                return -1         
                                         
    return total_bribes

    
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.lists = [[2, 1, 5, 3, 4], [5, 1, 2, 3, 7, 8, 6, 4], [1, 2, 5, 3, 7, 8, 6, 4], []]
        self.answers = [3, -1, 7, 0]

    def test_1(self):
        self.assertTrue(minimum_bribes(
            self.lists[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(minimum_bribes(
            self.lists[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(minimum_bribes(
            self.lists[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(minimum_bribes(
            self.lists[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main() 
