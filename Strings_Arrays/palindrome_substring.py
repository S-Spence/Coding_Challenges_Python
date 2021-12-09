import math
def longestPalindrome(s: str) -> str:
        
    """reverse_string = []
    longest_palindrome = ""
        
    for i in range(len(s)-1, 0, -1):
        reverse_string.append(s[i])
        
    for i in range(0, len(s)):
        if s[i] == reverse_string[i]:"""
    longest_palindrome = ""
    sub_string = ""
    rev_string = ""


    for i in range(len(s)):
        if i == 0:
            longest_palindrome = s[i]
        else:
            j = i-1
            k = i+1
            palindrome = True
            while j >= 0 and k < len(s) and palindrome == True:
                if s[j] == s[k]:
                    palindrome = True
                    if len(s[j:k+1]) > len(longest_palindrome):
                        longest_palindrome = s[j:k+1]
                else:
                    palindrome = False
                j-=1
                k+=1
 




    """if len(s) <= 1:
        longest_palindrome = s

    # Fill substring
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = s[i:j+1]
            print(sub_string)
            # add all elements of the substring to the reverse string
            rev_string = sub_string[::-1]
            print(rev_string)       
            # Check for palindrome
            palindrome = True
            if sub_string != rev_string:
                palindrome = False
            print(palindrome)   
            if palindrome == True:
                if len(sub_string) > len(longest_palindrome):
                    longest_palindrome = sub_string"""
    return longest_palindrome

if __name__ == "__main__":

    string = "cbbd"

    print(longestPalindrome(string))
