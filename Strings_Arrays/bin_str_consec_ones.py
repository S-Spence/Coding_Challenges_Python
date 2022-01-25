import unittest
"""
Problem: Count Consecutive Ones in a Binary String Challenge
         Take a binary string and count the max occurences of consecutive ones.
Solution: Keep track of the maximum number of ones seen so far, and update this variable if the current string on ones is longer.
          Runtime: O(n), Space: O(1)
"""


def count_consec_ones(binary_str: str) -> int:
    """This function counts the consecutive ones in a binary string"""
    # Value to max ones and current consecutive ones
    max_ones = 0
    current_ones = 0
    # Count consecutive ones in a binary string
    for val in binary_str:
        # Reset current ones if hitting a zero
        if val == "0":
            current_ones = 0
            continue
        # Increment current ones if hitting a one
        elif val == "1":
            current_ones += 1
        # Check if the current ones are greater than max ones and update
        if current_ones > max_ones:
            max_ones = current_ones
        
    return max_ones


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "11100011",
            "0101010111",
            "11010101",
            "",
            "00000",
            "111111"
        ]

        self.answers = [3, 3, 2, 0, 0, 6]

    def test_1(self):
        self.assertTrue(count_consec_ones(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(count_consec_ones(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(count_consec_ones(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(count_consec_ones(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(count_consec_ones(
            self.s[4]) == self.answers[4])
    
    def test_6(self):
        self.assertTrue(count_consec_ones(
            self.s[5]) == self.answers[5])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
