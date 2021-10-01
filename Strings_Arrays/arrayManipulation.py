#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    
    # Create array
    array = [0 for i in range(n+1)]

    """Update the starting and ending element + 1. Add k to the start and subtract k 
       from the value after the end value"""
    for query in queries:
        a = query[0]-1
        b = query[1]
        array[a] += query[2] 
        array[b] -= query[2]

    """ Iterate through the array adding and subtracting numbers
        The maximum value obtained during this iteration is the max val in the updated 
        array """
    sum = 0
    max_val = 0
    for val in array:
        sum += val
        max_val = max(max_val, sum)
    return max_val
    

if __name__ == '__main__':
