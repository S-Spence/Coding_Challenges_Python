import unittest
"""
Problem: Take input for number of words in each string. Then, take input for two strings, one a note, and the other a magazine.
         Next, determine if you can form the note from the words in the magazine list.

         Hackerrank: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_r=internal-search

Solution: Use a dictionary to track the words in the magazine.
        Runtime: O(n + m), Space: O(n)

"""


# Complete the checkMagazine function below
def check_magazine(magazine: str, note: str) -> None:
    """Check if a randsom note can be made of words in a string."""
    if len(note) == 0:
        return False

    magazine_dict = {}

    # Put magazine into dictionary
    for letter in magazine:
        if letter in magazine_dict:
            magazine_dict[letter] += 1
        else:
            magazine_dict[letter] = 1 
    
    for letter in note:
        if letter not in magazine_dict:
            return False
        
    return True
    
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.magazine = ["there is a movie playing tonight, meet 5pm", "attack at dawn", ""]
        self.notes = ["meet tonight", "attack at dawn", "help"]
        self.answers = [True, True, False]

    def test_1(self):
        self.assertTrue(check_magazine(
            self.magazine[0], self.notes[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(check_magazine(
            self.magazine[1], self.notes[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(check_magazine(
            self.magazine[2], self.notes[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main() 
