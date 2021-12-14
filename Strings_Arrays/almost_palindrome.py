import unittest
"""
Problem: Given a string, determine if it is almost a palindrome. A string is almost a palindrome if it becomes a palindrome
        after remving one letter. Consider only alphanumeric characters and ignore case sensitivity. 

Step 1: Questions
        Do we consider a palindrome an almost palindrome? -> Yes, true if it is already a palindrome
Step 2: Tests
        "abcdefdba"  -> False
        "racecar" -> True
        "abccdba" -> True
        "" -> True
        "a" -> true
        "ab" -> True
Step 3: use two pointers to iterate from the outside. When reaching two values that do not match, generate two separate strings with
        each removed and see if you have a palindrome. Return true or false there.
Step 4: Coding
        The runtime of this solution is O(n). Despite the sub palindrome function, it only checks each element once. A duplication
        occurs if the first substring is not a palindrome, and then the second substrng is checked. We could call it O(n + k) 
        where k is the length of the substring. However, O(n) becomes the dominant term. The space complexity is O(1).
        This is optimal.
"""
def is_alpha(ch: str) -> bool:
    """Determine if the character is an alphanumeric character"""
    if ord(ch) >= 48 and ord(ch) <= 57:
        return True
    if ord(ch) >= 97 and ord(ch) <= 122:
        return True
    
    return False

def is_palindrome(s: str) -> bool:
    """Assuming a clean string coming in because altering is in other function. Worst case O(n) here."""
    p1 = 0
    p2 = len(s) -1
    while p1 < p2:
        # Skip non-alphanumeric characters
        if not is_alpha(s[p1]):
            p1 += 1
            continue
        if not is_alpha(s[p2]):
            p2 -= 1 
            continue

        if s[p1] != s[p2]:
            return False
        
        p1 += 1
        p2 -= 1
        
    return True

def almost_palindrome(s: str) -> bool:
    """
    Determine if one letter removed from a string can make a palindrome. Return true for current palindrome.
    Worst case O(n). 
    """
    p1 = 0
    p2 = len(s)-1

    s = s.strip(" ").lower()

    while p1 < p2:
        # Skip non-alphanumeric characters
        if not is_alpha(s[p1]):
            p1 += 1
            continue
        if not is_alpha(s[p2]):
            p2 -= 1 
            continue
        # Handle logic for skipping p1 and p2. Only test the substrings since outer elements are already checked.
        if s[p1] != s[p2]:
            test_1 = s[p1+1:p2+1]
            test_2 = s[p1:p2]
            # This will add at worst O(2n) one time because of returns. So, O(3n) -> O(n)
            if is_palindrome(test_1) or is_palindrome(test_2):
                return True
            else:
                return False
                     
        p1+=1
        p2-=1

    return True
            

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "abcdefdba",
            "racecar",
            "abccdba",
            "",
            "a",
            "abc"
        ]

        self.answers = [False, True, True, True, True, False]

    def test_1(self):
        self.assertTrue(almost_palindrome(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(almost_palindrome(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(almost_palindrome(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(almost_palindrome(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(almost_palindrome(
            self.s[4]) == self.answers[4])
    
    def test_6(self):
        self.assertTrue(almost_palindrome(
            self.s[5]) == self.answers[5])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
