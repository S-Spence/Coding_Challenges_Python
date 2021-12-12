import unittest
"""
Problem: This problem asks to return the length of the longest substring of a given string. S consists of letters, numbers,
         symbols and characters. 

Step 1: Questions
        -> Is the substring contiguous? -> Yes, for a substring but not a subsequence. 
        substring vs subsequence. For a substring, characters do not have breaks. Subsequences can have breaks between the characters.
        -> Does case sensitivity matter? -> No, assume all lowercase (always ask this for string questions).
Step 2: Test Cases
        s: "abccabb" -> 3
        s: "" -> 0
        s: "cccccc" -> 1
        s: "pwwkew" -> 3
        s: "abcbda" -> 4
Step 3: Brainstorm solutions.
        The substrings can be overlapping. 
        Brute force solution. Use a nested for loop and iterate through the values, keeping track of a dictionary
        on every outter loop. Determine if the value is in the dict already, and increase length variable.
        O(n^2) time complexity. O(n) space complexity where k is the longest subarray.
        Optimized Approach: sliding window -> Time O(n). Space O(n)
"""
"""
def longest_no_repeats(s):
    #Brute force solution. 
    longest = 0
    "abccabb -> 3" 
    
    # Return 0 if string is empty
    if len(s) == 0:
        return longest 

    # nested for loop to check if the values have been seen before. Time complexity O(n^2), space complexity O(n) because the dictionary
    # gets reset each time and never exceeds n.
    for i in range(len(s)):
        seen_chars = {} 
        current = 0
        for j in range(i, len(s)):
            if s[j] not in seen_chars.keys(): 
                current += 1 # 1 -> 2 -> 3 ->-> 1 -> 2 ->-> 1 ->-> 1 -> 2 -> 3 ->-> 1 -> 2 ->-> 1 ->-> 1
                seen_chars[s[j]] = True # {a: true} -> {a: true, b: true} -> {1: true, b: true, c:true} ->->
                                        # {b: true} -> {b: true, c: true} ->->
                                        # {c: true} ->->
                                        # {c: true} -> {c: true, a:true} -> {c: true, a:true, b: true} ->->
                                        # {a: true} -> {a: true, b:true} ->->
                                        # {b: true} ->->
                                        # {b: true}
                longest = max(current, longest) # 1 -> 2 -> 3 ->-> 3 -> 3 ->-> 3 ->-> 3 -> 3 -> 3 ->-> 3 -> 3 ->-> 3 ->-> 3
            else:
                break
    return longest
"""
"""
Optimal solution uses the sliding window technique. Hint: use the sliding window to represent the current substring.
Drop the values off the left side of the substring when reaching a duplicate. 

"""
def longest_no_repeats(s):
    """Optimized solution. Time complexity O(n), Space complexity O(n). """
    # Return if the string is 1 char of less
    if len(s) <= 1:
        return len(s)
    # Create a dictionary for seen characters, left pointer, and longest string
    seen_chars = {}
    left_p = 0
    longest = 0

    "Manual Test Example: abccabb -> 3" 
    for right_p in range(len(s)):
        current_char = s[right_p] # a -> b -> c -> c -> a -> b -> b
        # If we have seen the current character before, check if the index is before the left pointer. If so, move left pointer. 
        if current_char in seen_chars.keys():
            prev_seen_index = seen_chars[current_char] # 2 -> 0 -> 1 -> 5
            if prev_seen_index >= left_p: # 2 > 0 -> 5 > 3
                # Move the left pointer ahead of the previously seen character
                left_p = prev_seen_index + 1 # 3 -> 5
        # Update or assign new index
        seen_chars[current_char] = right_p # {a: 0} -> {a: 0 , b: 1} -> {a: 0, b: 1, c: 2} -> {a: 0, b: 1, c: 3} 
                                            # -> {a: 4, b; 1, c: 3} -> {a: 4, b: 5, c: 3} -> {a: 4, b: 6, c: 3}
        # Determine current longest
        longest = max(longest, right_p - left_p + 1) # 1 -> 2 -> 3 -> 3 -> 3 -> 3 -> 3

    return longest 

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.s = [
            "abccabb",
            "",
            "ccccccc",
            "pwwkew",
            "abcbda"
        ]

        self.answers = [3, 0, 1, 3, 4]

    def test_1(self):
        self.assertTrue(longest_no_repeats(
            self.s[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(longest_no_repeats(
            self.s[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(longest_no_repeats(
            self.s[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(longest_no_repeats(
            self.s[3]) == self.answers[3])

    def test_5(self):
        self.assertTrue(longest_no_repeats(
            self.s[4]) == self.answers[4])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
