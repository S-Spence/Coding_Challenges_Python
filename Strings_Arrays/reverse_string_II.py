import unittest
"""
Problem: Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters.
        Return the reverse string of words with a single space between words. 
Step 1: Constraints
        Can there be multiple spaces between words? -> Yes, and trailing spaces
        Will the string ever be empty? -> No
Step 2: Tests
    "Hello         sir how are you   " -> "you are how sir hello"
    "         hello" -> "hello"
    "hello you" -> "you hello"
Step 3: convert to python list. Two pointer approach from both ends to modify in place. Convert back to string with spaces.
Step 4: Runtime: O(n), space: O(n) 
"""

def reverse_string_II(s: "list[str]")-> "list[str]":
    """Reverse the words in a string"""
    # Remove whitespace and convert to list of word. Runtime O(n), space O(n)
    arr = s.strip().split()

    p1 = 0
    p2 = len(arr)-1
    # Runtime O(n)
    while p1 < p2:

        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp

        p1 += 1
        p2 -= 1
    # Runtime O(n) to convert
    return " ".join(arr)

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "hello           sir how are you",
            "      hello",
            "hello again"
        ]

        self.answers = ["you are how sir hello", "hello", "again hello"]

    def test_1(self):
        self.assertTrue(reverse_string_II(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(reverse_string_II(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(reverse_string_II(
            self.s[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
