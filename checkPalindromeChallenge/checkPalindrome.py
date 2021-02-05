#!/usr/bin/python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-02-05
# Title: Check Palindrome
# Description: This function takes string input and uses the methods in the checkPalindromeClass file to check if the string is a
#              palindrome. This is the project run script. 
#---------------------------------------------------------------------------------------------------------------------------------------
import sys
import os
import checkPalindromeClass as cp

def main():   
    # read the string s
    s = input()
    #Create the Solution class object
    obj= cp.checkPalindrome()   

    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])
    
    isPalindrome=True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    for i in range(l // 2):
        if obj.popCharacter()!=obj.dequeueCharacter():
            isPalindrome=False
            break
    #finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")  

if __name__ == "__main__":
    sys.exit(main())
