#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-01-25
# Title: Count Consecutive Ones in a Binary String Challenge
# Description: Take an integer n and convert it to a binary string. Then, count the max occurences of consecutive ones in the 
#              binary string.
#---------------------------------------------------------------------------------------------------------------------------------------
import sys


# Find max consecutive ones in a binary string
def count_consec_ones(binary_str: str) -> int:
    """This function counts the consecutive ones in a binary string"""
    # Value to count ones
    max_ones = 0   
    # Strip leading and trailing zeros and split at zeros
    binary_str = binary_str.strip("0").split("0")
    # Count consecutive ones
    for str in binary_str:
        if len(str) > max_ones:
            max_ones = len(str)
    return max_ones


# Main function   
def main() -> None:
    """Main function for quick testing"""
      # Take integer input
    num = int(input())
    # Return the binary representation of the integer n
    binary_rep = "{0:b}".format(num)
    # Print highest occurence of consecutive ones
    max_consec = count_consec_ones(binary_rep)
    print(max_consec)
    return


if __name__ == '__main__':
    sys.exit(main())   
