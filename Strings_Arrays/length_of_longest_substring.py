def lengthOfLongestSubstring(s: str) -> int:
    """A method to determine the longest substring with unique values in a string"""
    unique_list = set() # Create a set to store unique string values
    longest_str = 0 # Longest substring
    if len(s) == 1:
        return 1
    if len(s) == len(set(s)):
        return len(s)
    sets = []
    # loop through the values of s and append values to the set
    for val in range(len(s)):
        starting_length = len(unique_list)
        unique_list.add(s[val])
        ending_length = len(unique_list)
            
        # If the set's starting and ending length were the same, the unique string is broken
        if starting_length == ending_length:
            # Set new longest substring to set size and reset to an empty set
            unique_list = set()
            val = val - ending_length + 1 # Backtrack to check the next substring
            unique_list.add(s[val])
        
        sets.append(unique_list)
            
        if ending_length > longest_str:
            longest_str = ending_length
        
    return longest_str, sets
def lengthOfLongestSubstring2(s: str) -> int:
    def check(start, end):
        chars = [0] * 128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1
            if chars[ord(c)] > 1:
                return False
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


s = "dvdf"
a = "abcabcbb"
v = "PPPPPPbbghgjkshkhgshlkkkkk"
print(lengthOfLongestSubstring2(v))
