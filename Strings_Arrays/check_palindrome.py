import unittest
import re
"""
Problem: Check if a string is a valid palindrome.

Step 1: Questions
        Does case sensitivity matter? -> No
        Will the string only contain letters? -> No
        How to handle symbols? -> ignore symbols and whitespace in the string.
        What to return for 0 and 1 character? -> False for 0 True for 1
Step 2: Strategy shifting pointers. Start at either end and meet in the middle. Break if reaching two letters that dont match.
        Define a helper function to determine if a char is alphanumeric. Remove whitespace.
Step 3: Define test cases "a man, a plan, a canal, panama." -> true
                          " Havah" -> true
                          "my fair lady" -> false
                          "" -> false
Step 4: Code. Brute force runtime with shifting pointers O(n). Space O(1). 
Step 5: Optimize. 
    This was a good solution for the first try. However, it helps to know other ways of approaching palindrome questions because
    strategies dont work for each question. 
    Another method would have been to start both pointers at te center and work out. If
    the string were even in this case, the pointers would intialize at two separate center points. I like the first method because
    if saves the conditional checks.
    A third method would be to create a copy of the string in reverse and compare strings. However, this is still O(n) and now O(n)
    additional space also. First solution is O(1) space. 
"""

def is_alpha(ch: str) -> bool:
    """Determine if the char is 0-9 or [a-z]"""
    if ord(ch) >= 48 and ord(ch) <= 57:
        return True
    if ord(ch) >= 97 and ord(ch) <= 122:
        return True
    return False


def is_palindrome(s: str) -> bool:

    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    
    # Test: A man, a plan, a canal, panama -> true
    s = s.strip(" ").lower()
    p1 = 0
    p2 = len(s) - 1  # 23
    # Test: aman,aplan,acanal,panama
    while (p1 < p2):
        # if either value is not alphanumeric, shift the pointer and skip the rest of this loop
        if is_alpha(s[p1]) == False:
            p1 += 1  # 5 -> 11
            continue
        if is_alpha(s[p2]) == False:
            p2 -= 1  # 16
            continue

        if s[p1] != s[p2]:
            return False
        p1 += 1  # 1 -> 2 -> 3 -> 4 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12
        p2 -= 1  # 22 -> 21 -> 20 -> 19 -> 18 -> 17 -> 15 -> 14 -> 13 -> 12
    return True


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "A man, a plan, a canal, panama",
            "",
            "Havah ",
            "my fair lady",
            "atesting"
        ]

        self.answers = [True, False, True, False, False]

    def test_1(self):
        self.assertTrue(is_palindrome(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(is_palindrome(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(is_palindrome(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(is_palindrome(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(is_palindrome(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
