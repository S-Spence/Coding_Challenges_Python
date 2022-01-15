import unittest
"""
Problem: Implement the my Atoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for my atoi is as follows
1. Read in and ignore any leading whitespace
2 Check if the next character, if not already at the end of the string is "-" or "+". Read this character in if it is either. 
This determines if the final result is negative or positive. If neither is present, the result is positive.
3. Read in the characters until the next non-digi character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e: "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range, [-2^31, (2^31-1)], then clamp the integer so it remains in the
range. Specifically, integers less than -2^31 should be clamped to that value. Same for the max value.
6. Return the integer as the final result

Leetcode: https://leetcode.com/problems/string-to-integer-atoi/

Constraints: 
            What to return when the string is empty? -> 0

"""


def my_atoi(s: str) -> int:
    """
    Convert the digits at the beginning of a string to a 32-bit integer.
    Runtime: O(n), Space: O(1)
    """
    # Values to store the values and the sign
    result = 0
    sign = 1
    # index and length
    index = 0
    n = len(s)
    # min an max values
    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)

    # Skip whitespace
    while index < n and s[index] == " ":
        index += 1
    # Adjust sign
    if index < n and s[index] == "+":
        index += 1
    elif index < n and s[index] == "-":
        sign = -1
        index += 1
    # Convert to digit
    while index < n and s[index].isdigit():
        digit = int(s[index])
        # Check for overflows and underflows. Dividing by ten garantees that any number added would be less than int max
        if (result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN

        # Append current digit to the result.
        result = 10 * result + digit
        index += 1

    # Multiply the value by its sign and return
    return sign * result


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "        42",
            "34455 hello",
            "33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
        ]

        self.answers = [42, 34455, pow(2, 31) - 1]

    def test_1(self):
        self.assertTrue(my_atoi(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(my_atoi(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(my_atoi(
            self.s[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
