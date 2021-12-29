import unittest
"""
Problem: Find the longest palindromic substring. The string will contain only alphanumeric chars.

Step 1: Constaints
    there will only be one substring of the longest length in the string
    Case sensitive? -> Yes

Step 2: "abbcd" -> "bb"
        "b" -> "b"
        "" -> ""

Step 3: Solutions

    Method 1: Dynamic Programming. Time: O(n^2), Space: O(n^2)
    Method 2: Mirror around every center --Space Optimization. Time: O(n^2), Space: O(1)
    Method 3: Manacher's algotirhm. Time: O(n), space: O(n)

"""


def longest_pal_substr_1(s: str):
    """Method 1: Dymanic programming. Time: O(n^2), Space: O(n^2)"""
    # get length of string
    length = len(s)
    """ 
    Create a table to track substring [i..j].
    Ex: ABBE
      A B B E
    A 1 0 0 0
    B 0 1 1 0
    B 0 0 1 0
    E 0 0 0 1
    
    bb is the longest palindrome
    """
    # Initialize table of zeros
    table = [[0 for x in range(length)] for y in range(length)]

    # Elements along the diagonal are always true because the letters form palindromes with themselves.
    for i in range(len(s)):
        table[i][i] = 1
    # The longest palindrome to start is 1
    max_length = 1
    start = 0

    # Test ABBC starting table below
    #   A B B C
    # A 1 0 0 0
    # B 0 1 0 0
    # B 0 0 1 0
    # C 0 0 0 1
    # i = 2 -> 3 -> 4
    for i in range(2, len(s)+1):
        # j = 0 -> 1 -> 2 ->-> 0 -> 1 ->-> 0
        for j in range(len(s)-i+1):
            end = j+i  # 2 -> 3 -> 4 ->-> 3 -> 4 ->-> 4

            if i == 2:
                # if there is a palindrome, update table, update length, update start
                if s[j] == s[end-1]:
                    table[j][end-1] = 1  # table[1][2] = 1
                    max_length = i    # 2
                    start = j         # 1
            else:
                # if there is a palindrome, update table, update length, update start
                if s[j] == s[end-1] and table[j+1][end-2]:
                    table[j][end-1] = 1
                    max_length = i
                    start = j
    # Test table after
    #   A B B C
    # A 1 0 0 0
    # B 0 1 1 0
    # B 0 0 1 0
    # C 0 0 0 1

    # return the starting index to max length + start
    return s[start:start+max_length]


def longest_pal_substr_2(s: str) -> str:
    """Method 2: Mirror around center at every value. Space Optimization O(1), runtime: O(n^2)"""
    # Manual test: "abbc"
    # Initialize max to 1
    max_length = 1
    # Initialize start and length
    start = 0
    length = len(s)  # 4

    low = 0
    high = 0

    # One by one consider every character as center point of even and odd length palindromes
    # Testing "abbc"
    # 1 -> 2 -> 3
    for i in range(1, length):
        """ Find the longest even length palindrome with center points as i-1 and i """
        low = i - 1  # 0 -> 1 -> 2
        high = i    # 1 -> 2 -> 3

        # Shift pointers while there is a palindrome within boundaries
        # s[0] = s[1]? no -> s[1] = s[2]? yes -> s[30] = s[3]? no -> s[2] = s[3]? no
        while low >= 0 and high < length and s[low] == s[high]:
            low -= 1  # 0
            high += 1  # 3

        # Move back to the last possible valid palindrome substring as that will anyway be the longest from above loop
        low += 1  # 1 -> 1 -> 3
        high -= 1  # 0 -> 2 -> 2

        # Update start and max length if the current palindrome is greater than the max
        # s[1] = s[0]? no -> s[1] = s[2] and 2> 1? yes -> s[3] = s[2]? no
        if s[low] == s[high] and high - low + 1 > max_length:
            start = low                 # 1
            max_length = high - low + 1  # 2

        """ Find the longest odd length palindrome with center point as i """
        low = i - 1  # 0 -> 0 -> 2
        high = i + 1  # 1 -> 3 -> 3

        # While there is a palindrome within the boundary, shift pointers
        # s[0] = s[1]? no -> s[0] = s[3]? no -> s[2] = s[3]? no
        while low >= 0 and high < length and s[low] == s[high]:
            low -= 1
            high += 1

        # Move back to the last possible valid palindrome substring as that will anyway be the longest from above loop
        low += 1  # 1 -> 1 -> 4
        high -= 1  # 0 -> 2 -> 1

        # Update start and max_length if the current palindrome is the longest
        # s[1]= s[2] and 2 > 2? no s[4] = s[1]? no
        if s[low] == s[high] and high - low + 1 > max_length:
            start = low
            max_length = high - low + 1

    # Return start to start+max_length
    # "abbc" -> s[1: 1+2] -> s[1:3] = "bb"
    return s[start:start + max_length]


def longest_pal_substr_3(s: str) -> str:
    """
    Manacher's Algorithm: Time O(n), space: O(n). 
    Mirrors around a unique center.
    An even lengh string does not have a unique center.
    Add a unique character (# is common) at the start, end, and in between every char of the string to prevent even strings.
    """
    # Test "abbc"
    # Insert special char # at start, end and in between every character of s. Space/time O(n)
    new_string = "#" + "#".join(s[i:i + 1] for i in range(0, len(s), 1)) + "#"  # "#a#b#b#c#"
    # Create a list of zeros to track longest pal substring. Space/Time = O(2n+1) = O(n)
    lps = [0 for _ in range(len(new_string))]  # [0, 0, 0, 0, 0, 0, 0, 0]
    # Initialize center and right pointers to zero
    center = 0
    length = 0

    # Manual Test -> "#a#b#b#c#"
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
    for i in range(len(new_string)):
        mirror = 2*center - i  # 0 -> -1 -> 0 -> -1 -> 2 -> 3 -> 2 -> 1 -> 6

        if length > i:
            lps[i] = min(length-i, lps[mirror])  # lps[5] = 1

        try:
            # s[1] = s[0]? no -> s[2] = s[0]? yes -> s[4] = s[-1]? pass -> s[3] = s[1]? no -> s[4] = s[2]? yes
            # -> s[5] = s[1]? no -> s[5] = s[3]? yes -> s[6] = s[4]? yes -> s[7] = s[3]? no
            # -> s[7] = s[3]? no -> s[7] = s[5] -> no -> s[8] = s[6]? yes -> s[9] = s[5]? pass
            # -> s[9] = s[7]? pass
            while new_string[i + 1 + lps[i]] == new_string[i - 1 - lps[i]]:
                # lps[1] = 1 -> lps[3] = 1 -> lps[4] = 1 -> lps[4] = 2 -> lps[7] = 1
                lps[i] += 1
        except:
            pass

        if i + lps[i] > length:
            center = i         # 1 -> 3 -> 4 -> 7
            length = i + lps[i]  # 2 -> 4 -> 6 -> 8

    length = max(lps)             # 2
    center = lps.index(max(lps))  # 4
    # new_str = "#a#b#b#c#" -> s[2:6] = "#b#b#" -> "bb"
    return new_string[center - length: center + length].replace("#", "")


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "",
            "abbc",
            "racecar",
            "b"
        ]

        self.answers = ["", "bb", "racecar", "b"]

    # First approach. DP
    def test_1(self):
        self.assertTrue(longest_pal_substr_1(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(longest_pal_substr_1(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(longest_pal_substr_1(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(longest_pal_substr_1(
            self.s[3]) == self.answers[3])

    # Second approach

    def test_5(self):
        self.assertTrue(longest_pal_substr_2(
            self.s[0]) == self.answers[0])

    def test_6(self):
        self.assertTrue(longest_pal_substr_2(
            self.s[1]) == self.answers[1])

    def test_7(self):
        self.assertTrue(longest_pal_substr_2(
            self.s[2]) == self.answers[2])

    def test_8(self):
        self.assertTrue(longest_pal_substr_2(
            self.s[3]) == self.answers[3])

    # Third approach

    def test_9(self):
        self.assertTrue(longest_pal_substr_3(
            self.s[0]) == self.answers[0])

    def test_10(self):
        self.assertTrue(longest_pal_substr_3(
            self.s[1]) == self.answers[1])

    def test_11(self):
        self.assertTrue(longest_pal_substr_3(
            self.s[2]) == self.answers[2])

    def test_12(self):
        self.assertTrue(longest_pal_substr_3(
            self.s[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main()
