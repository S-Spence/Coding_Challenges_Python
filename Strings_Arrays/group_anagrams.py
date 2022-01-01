import unittest
"""
Problem: Given an array of strings, group the anagrams together and return an array of arrays containing the groupings.
         Leetcode: https://leetcode.com/problems/group-anagrams/

Constraints: 
            What to return if list is empty? -> The list will not be empty
            Case sensitive? -> Assume all letterd are lower
Tests: 
    ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"] -> ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
    ["eat","tea","tan","ate","nat","bat"] -> [["eat", "tea", "ate], ["tan", "nat"], ["bat"]]
    ["ac", "c"] -> [["ac"], ["c"]]
    
Solutions:
        Solution one: Create a dictionary that uses the sorted strings as keys to map all anagrams to the correct buckets.
        This solution has a runtime of O(nklogk) due to sorting. The space complexity is O(nk) where k is the length of the
        longest word. 

        Solution two: Create a dictionary that uses a string representation of the word using letter counts to map 
        anagrams to the same bucket. Runtime: O(nk), Space: O(nk), where k is the length of the longest word.
"""


def group_anagrams(strs: "list[str]") -> "list[list[str]]":
    """Group Anagrams. Runtime: O(nklogk), Space: O(nk) where k is the case of the longest word"""
    anagrams = {}

    # Create a dictionary of anagrams mapped by their sorted value
    # O(n)
    for val in strs:
        # sort list O(klogk)
        sorted_val = str(sorted(val))

        if sorted_val in anagrams:
            anagrams[sorted_val].append(val)
        else:
            anagrams[sorted_val] = [val]

    return list(anagrams.values())


def group_anagrams_2(strs: "list[str]") -> "list[list[str]]":
    """
    Group Anagrams using a dictionary to store stings representing the alphabet. 
    If the strings have the same alphabetic representation, they map to the same bucket.
    Runtime: O(nk), space: O(nk) where k is the longest word.
    """
    # Define a dictionary to group anagrams
    anagrams = {}
    # Loop through values in string list O(n)
    for val in strs:
        # Initialize an array representation of the alphabet for every calue, keeping a count of letters in a string. Space O(26)
        chars = [0] * 26
        # Runtime O(k) where k is the longest word
        for letter in val:
            index = ord(letter) - ord("a")
            chars[index] += 1
        # Convert the list to a string act as a key
        key = str(chars)
        # Fill the dictionary to identify anagrams
        if key in anagrams:
            anagrams[key].append(val)
        else:
            anagrams[key] = [val]
    # Return anagrams
    return list(anagrams.values())


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.strs = [
            ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"],
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            ["ac", "c"]
        ]

        self.answers = [
            [["cab"], ["tin"], ["pew"], ["duh"], ["may"], [
                "ill"], ["buy"], ["bar"], ["max"], ["doc"]],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            [["ac"], ["c"]]
        ]

    # First approach. Sorting
    def test_1(self):
        self.assertTrue(group_anagrams(
            self.strs[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(group_anagrams(
            self.strs[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(group_anagrams(
            self.strs[2]) == self.answers[2])
    # Second approach

    def test_4(self):
        self.assertTrue(group_anagrams_2(
            self.strs[0]) == self.answers[0])

    def test_5(self):
        self.assertTrue(group_anagrams_2(
            self.strs[1]) == self.answers[1])

    def test_6(self):
        self.assertTrue(group_anagrams_2(
            self.strs[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
