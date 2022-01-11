import unittest
"""
Problem: given a string representing a roman numeral, convert it to an integer.
        Leetcode: https://leetcode.com/problems/roman-to-integer/
Constraints: 
        What to return if the string is empty? -> -1

Solution: Use a dictionary to represent the rules. Runtime: o(n), Space: O(1)

"""


def roman_to_int(s: str) -> int:
    """Convert roman to integer. Time: O(n), Space: O(1)"""
    # Roman to integer rules
    rules = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # if string is empty, return 0
    if len(s) == 0:
        return -1
    # if there is only one values, return value
    if len(s) == 1:
        return rules[s]
    # initialize total
    total = 0

    # any time the value before is less than the values, subtract, else add
    # "MCMXCIV"
    # c -> m -> x -> c -> i -> v
    for i in range(1, len(s)):
        # subtract or add based on value
        if rules[s[i]] > rules[s[i-1]]:
            total -= rules[s[i-1]]  # 900 -> 1890 -> 1989
        else:
            total += rules[s[i-1]]  # 1000 -> 1900 -> 1990
        # if it is on the final value, add to total
        if i == len(s)-1:
            total += rules[s[i]]  # 1994

    return total


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "",
            "MCMXCIV",
            "LVIII",
            "XXVII",
            "III"
        ]

        self.answers = [-1, 1994, 58, 27, 3]

    def test_1(self):
        self.assertTrue(roman_to_int(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(roman_to_int(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(roman_to_int(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(roman_to_int(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(roman_to_int(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main()
