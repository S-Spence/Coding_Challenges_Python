#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence & Copyright: HackerRank
# Date: 2021-02-05
# Title: Check Palindrome
# Description: This function takes string input and uses the methods in the checkPalindromeClass file to check if the string is a
#              palindrome. This is the project run script. 
#---------------------------------------------------------------------------------------------------------------------------------------
import sys
import os
import checkPalindromeClass as cp


# Main function
def main() -> None:  
    """Main function to check if a string is a palindrome"""
    # read the string s
    s = input()

    # Create the check palindrome class object
    obj= cp.CheckPalindrome()   

    length = len(s)

    # Push/enqueue all the characters of string s to stack
    for i in range(length):
        obj.push_character(s[i])
        obj.enqueue_character(s[i])
    
    is_palindrome = True

    """
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    """
    for i in range(length // 2):
        if obj.pop_character() != obj.deque_character():
            is_palindrome = False
            break
    
    # Finally print whether string s is palindrome or not.
    if is_palindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")  
    return


if __name__ == "__main__":
    sys.exit(main())
