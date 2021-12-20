import unittest
"""
Problem: Given a string containing only parentheses, determine if the string is valid. If valid, all opened parentheses are closed.
        Leetcode (Easy): https://leetcode.com/problems/valid-parentheses/
Step 1: Constraints:
    All types of parantheses {}[]()? -> yes
    Will the string have whitespace? -> it could
    Does an empty string count as valid? -> yes 
Step 2: Tests:
    "" -> True
    "{([])}" -> True
    "{([])]" -> False
    "{[()}}" -> False
    "{()[]}" -> True
Step 3: Solution
    A stack may be helpful here becuase the order in which you must pull the matching bracke out of the stack matters.
    The opening brace should be the last item added to the stack.
Step 4: Runtime: O(n) Space O(n)
"""

def valid_parentheses(s: str)->bool:
    """Determine if a string contains valid parentheses"""
    stack = [] # Use an array for stack, space O(n)
    # Define a dictionary to store valid parentheses O(3) drop constants, this is not very significant memory usage
    valid = {
        "{":"}",
        "[":"]",
        "(":")"
    }
    # Remove whitespace from string
    s = s.replace(" ", "")
    # Return true if string is empty
    if len(s) == 0:
        return True
    # Return false if string length is uneven
    if len(s) % 2 != 0:
        return False

    # Time: O(n)
    # Test "{([])}" -> True
    # { -> ( -> [ -> ] -> ) -> }
    for i in range(len(s)):
        val = s[i] # { -> ( -> [ -> ] -> ) -> }
        if val in valid.keys():
            stack.append(val) # -> [ { ] -> [ {, ( ] -> [ {, (, [ ]
        # Only pop the stack if elements exist
        elif val in valid.values():
            # Return false if there is a closing bracket with no opener
            if len(stack) == 0:
                return False

            opening = stack.pop() # ] -> ) -> }
            # If the closer does not match the last opener, return false
            if s[i] != valid[opening]:
                return False
    # If the stack is not empty, return false.
    if len(stack) != 0:
        return False
    else:
        return True # Test case returns true


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "",
            "{([])}",
            "{([])]",
            "{[(}}",
            "{()[]}",
            "))"
        ]

        self.answers = [True, True, False, False, True, False]

    def test_1(self):
        self.assertTrue(valid_parentheses(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(valid_parentheses(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(valid_parentheses(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(valid_parentheses(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(valid_parentheses(
            self.s[4]) == self.answers[4])
    def test_6(self):
        self.assertTrue(valid_parentheses(
            self.s[5]) == self.answers[5])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
