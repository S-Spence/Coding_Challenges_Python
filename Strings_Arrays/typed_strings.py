import unittest
"""
Given two strings S and T, determine if they are equal when typed out. Any '#' that appears in the string counts as a backspace.
Leetcode (easy): 

Ex: "cb#d" -> "cd" therefore, the # deletes the character before it. 

Step 1: Questions
        What happens if a # appears when there is no symbol to remove? -> It deletes nothing
        Are two empty strings equal? -> Yes
        Does case sensitivity matter? -> Yes
Step 2: Test Cases
                -> s: "ab#z" t: "az#z" -> true
                -> s: "abc#d" t: "acc#c" -> false
                -> s: "x#y#z#" t: "a#" -> true
                -> s: "a###b" t: "b" -> true
                -> s: "Ab#c" t: "ab#z" -> false 
Step 3: Solutions: 
        -> One way to do this would be to modify the strings, however, strings are immutable so this would make a copy of the strings.
        -> Another way would be to loop backwards and skip the next value if there is a # infront of it. Return false
        at any time if the letters dont match and there is no hash. Additonaly space = O(nk) where k is elements in t and n is elements
         in s. 

         Brute force solution was : O(a + b) space, O(a + b) time. This is a pretty good solution. You may be able to optimize space.

         Hint: utilize the original strings instead of creating new arrays
               Try use two pointer technique

"""

def modify_string(s: str) -> "list[str]":
    # Create a helper function to modify the string and return an array according to the # rule
    new_array = []
    for i in range(len(s)):
        # If we are on the last element there is no i+1
        if s[i] != "#":
            new_array.append(s[i])
        elif len(new_array) != 0:
            new_array.pop()
    return new_array

"""
def matching_strings(s: str, t: str) -> bool:
    # Call the helper function to modify the strings and compare output.
    new_s = modify_string(s)  # O(a) time
    new_t = modify_string(t)  # O(b) time
    matching = False
    # manual test -> s: "ab#z" t: "az#z" -> true
    # s -> [a] -> [a] -> [a] -> [a, z]
    # t -> [a] -> [a] -> [a] -> [a, z]

    # Check if the strings match
    # test -> [a, z] = [a, z]
    # you do not need to run an O(n) list comparison if the lists are not equal length. Length check O(1)
    if len(new_s) != len(new_t):
        matching = False
    # Python list comparison is O(n). Worst case here will either be O(a) or O(b) neither list will exceed its original length.
    elif new_s == new_t:
        matching = True

    return matching
"""

"""Final Time Complexity brute force -> O(2a + 2) or O(a + 2b). Either way, drop the constant and it is O(a + b)"""


# This code does not work. Out of range error. Fails some test cases when working around it.

def backspace(s: str, index: int) -> int:
    if s[index] == '#':
        backcount = 2
        while backcount > 0 and index > 1:
            index -= 1 # 2, 1, 0, -1
            backcount -= 1 # 1, 0, 1, 0
            if index >= 0:
                if s[index] == '#':
                    backcount += 2
    return index

def matching_strings(s: str, t: str) -> bool:
    #Optimized solution uses two pointers and shifts the pointers according to # symbols
    # Test s: "ab##" t: "a#b#"
    p1 = len(s)-1  # 3 ->
    p2 = len(t)-1  # 3 ->

    while p1 >= 0 and p2 >= 0:

        
        # Move pointers if one of the values is a hash
        if s[p1] == "#" or t[p2] == "#":  #, # ->
            # This won't shift anything if there is no #
            p1 = backspace(s, p1) # -1
            p2 = backspace(t, p2) # -1
        
        # Else, decrement each pointer by one
        else:
            p1 -= 1
            p2 -= 1
    return True


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "ab#z",
            "abc#d",
            "x#y#z#",
            "a###b",
            "Ab#c",
            "ab##",
            "a#c###"
        ]      
        self.t = [
            "az#z",
            "acc#c",
            "a#",
            "b",
            "ab#z",
            "c#d#",
            "ad#c"
        ]
        self.answers = [True, False, True, True, False, True, False]

    def test_1(self):
        self.assertTrue(matching_strings(
            self.s[0], self.t[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(matching_strings(
            self.s[1], self.t[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(matching_strings(
            self.s[2], self.t[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(matching_strings(
            self.s[3], self.t[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(matching_strings(
            self.s[4], self.t[4]) == self.answers[4])

    def test_6(self):
        self.assertTrue(matching_strings(
            self.s[5], self.t[5]) == self.answers[5])
    def test_7(self):
        self.assertTrue(matching_strings(
            self.s[6], self.t[6]) == self.answers[6])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
