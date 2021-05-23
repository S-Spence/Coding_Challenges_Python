#!/usr/bin/env python
# -----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-01-20
# Title: Randsom Note Challenge
# Description: Take input for number of words in each string. Then, take input for two strings, one a note, and the other a magazine.
#              Next, determine if you can form the note from the words in the magazine list.
#---------------------------------------------------------------------------------------------------------------------------------------
import sys
from collections import Counter


# Complete the checkMagazine function below
def check_magazine(magazine: str, note: str) -> None:
    """Check if a randsom note can be made of words in a string."""
    magazine_dict = dict()
    note_dict = dict()
    
    # Put lists into dictionaries
    for letter in magazine:
        if letter in magazine_dict:
            magazine_dict[letter] += 1
        else:
            magazine_dict[letter] = 1 
    
    for letter in note:
        if letter in note_dict:
            note_dict[letter] += 1
        else:
            note_dict[letter] = 1
        
    # Remove all matches from randsom note, returns empty dict if all matches found
    remove_matches = note_dict - magazine_dict
    
    # Check if list is empty
    if remove_matches:
        print("No")
    else:
        print("Yes")
    return
    
       
def main() -> None:

    # Take string input for the number of words in a magazine, and the number of words in a note, separate by a space
    mn = input().split()

    # Number of words in magazine
    m = int(mn[0])

    # Number of words in note
    n = int(mn[1])

    # Turn string input into a list by splitting at whitespace
    magazine = input().rstrip().split()

    # Turn note inpupt into a list by splitting at whitespace
    note = input().rstrip().split()

    # Check if the note can be formed from the words in the magazine list
    check_magazine(magazine, note)
    return


if __name__ == '__main__':  
    sys.exit(main())
