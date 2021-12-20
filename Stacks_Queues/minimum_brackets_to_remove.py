import unittest
"""
Problem: Given a string that only contains round brackets, as well as lowercase characters, remove the least amount of brackets so that 
        the string is valid. A string is considered valid if it is empty or if all opening brackets close. 
        Leetcode (Medium): https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Step 1: Constraints
    What to return? Return a valid string with the fewest parentheses removed
    Will there ever be spaces in the string? -> No
    Is a string containing no parentheses valid also? -> Yes
Step 2: Tests
    "a)bc(d)" -> abc(d)
    "(ab(c)d" -> ab(c)d or (abc)d
    "))((" -> ""
    "(((((" -> ""
Step 3: Solution
    Add the opening parentheses to a stack. pop the stack everytime you see a closing element.
    If the stack if not empty, those are the number of opening brackets you must remove. Remove openers from the end to keep string
    valid.
    If the length of the stack ever equals zero when you try to pop, remove the current closing bracket because it has no
    matching opener.
Step 4: Code 
    Runtime: O(n), Space O(n)
"""

def remove_min_brackets(s: str)->str:

    stack = []        # A stack to store opening brackets. O(n) space.
    edit_string = [val for val in s] # List for string editing O(n) time and space
    new_string = ""   # String to return

    # O(n) runtime
    # Test "(ab(c)d" -> ab(c)d or (abc)d
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    for i in range(len(edit_string)):
        val = edit_string[i] # ( -> a -> b -> ( -> c -> ) -> d
        if val == "(":
            stack.append(val) # [ ( ] -> [ (, ( ]
        elif val == ")":
            # If there is no opening bracket, increment closing to remove
            if len(stack) == 0:
                # Set to an empty string here rather than removing because removing mid list is O(n) and replacing is O(1)
                edit_string[i] = ""
            else:
                stack.pop() # [ ( ]
    # Determine how many opening parentheses to remove
    extra_openers = len(stack)
    # Remove openers from the end instead of the beginning to keep strings valid
    # Loop from the back of the list (range to -1 because 0 is non-inclusive), step size -1, worst case O(n)
    for i in range(len(edit_string)-1, -1, -1):
        # Update list elements if they equal (
        if edit_string[i] == "(":
            edit_string[i] = ""
            extra_openers -= 1
        # Break if there are no more extra opening brackets
        if extra_openers == 0:
            break

    # Convert back to a string           
    new_string = new_string.join(edit_string)

    return new_string

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "((((((",
            "a)bc(d)",
            "(ab(c)d",
            "))((",
            "())()((("
        ]

        self.answers = ["", "abc(d)","ab(c)d", "", "()()"]
        self.answers_alt = ["(abc)d"]

    def test_1(self):
        self.assertTrue(remove_min_brackets(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(remove_min_brackets(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(remove_min_brackets(
            self.s[2]) == self.answers[2] or self.answers_alt[0])

    def test_4(self):
        self.assertTrue(remove_min_brackets(
            self.s[3]) == self.answers[3])
    def test_5(self):
        self.assertTrue(remove_min_brackets(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
