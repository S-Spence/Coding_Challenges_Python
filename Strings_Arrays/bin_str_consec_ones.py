import unittest
"""
Title: Count Consecutive Ones in a Binary String Challenge
Description: Take an integer n and convert it to a binary string. Then, count the max occurences of consecutive ones in the
              binary string.
"""


def count_consec_ones(binary_str: str) -> int:
    """This function counts the consecutive ones in a binary string"""
    # Value to count ones
    max_ones = 0
    # Strip leading and trailing zeros and split at zeros
    binary_str = binary_str.strip("0").split("0")
    # Count consecutive ones
    for str in binary_str:
        if len(str) > max_ones:
            max_ones = len(str)
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
