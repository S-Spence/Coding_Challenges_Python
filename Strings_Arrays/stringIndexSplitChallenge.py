#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-01-20
# Description: String split by even and odd index values
#              Take input for the number strings. split the strings by odd and even index values.
#              Next, print the characters with even indices as one word and the characters with odd incides as another word
#              Repeat for the number of strings the user passes
#---------------------------------------------------------------------------------------------------------------------------------------
import sys

# Take T strings and print the odd and even indexed integers on the same line, 
# separate by a space to split the evens and odds. 
def split_strings(str_list: list) -> None:
    """A function to split strings by odd and even indexes."""
    
    # Loop through words in list
    for word in str_list:
        even_str = ""
        odd_str = ""
    
        # Loop through letters in word
        for i in range(len(word)):
            
            # split letters by even and odd indices
            if i % 2 == 0:
                even_str += word[i]
            else:
                odd_str += word[i]
            i += 1
        
        print(f"{even_str} {odd_str}")
    return


def main() -> None:
    """Main function"""
    str_list = []
    
    # Take input for number of strings
    T = int(input())
    
    # Take string input and strip whitespace
    for i in range(T):
        str_list.append(input().replace(" ", ""))
    
    split_strings(str_list)

    return

if __name__ == '__main__':
    sys.exit(main())
