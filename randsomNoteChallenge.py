#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-01-20
# Description: Randsom Note Challenge
#              Take input for number of words in each string. Then, take input for two strings, one a note and one a magazine
#              Next, determine if you can form the note from the words in the magazine list
#---------------------------------------------------------------------------------------------------------------------------------------

from collections import Counter

# Complete the checkMagazine function below
def checkMagazine(magazine, note):
    
    # Use counter to count occurences of words in the lists
    # Remove all matches from randsom note, returns empty list if all matches found
    removeMatches = Counter(note) - Counter(magazine)
    
    # Check if list is empty
    if len(removeMatches) == 0:
        print("Yes")
    else:
        print("No")
    
       
if __name__ == '__main__':

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
    checkMagazine(magazine, note)
