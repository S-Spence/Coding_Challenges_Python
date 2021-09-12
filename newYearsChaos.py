#!/usr/bin/env python
import random

# Complete the minimumBribes function below.
def minimumBribes(q):
    total_bribes = 0     # Create a variable for total bribes

    # iterate backwards
    for i in range(len(q)-1, 0, -1):
        index = i + 1 # index for line starts at one
        
        if q[i] != index:
            # If i made one swap
            if i-1 >= 0 and index == q[i-1]:
                temp = q[i-1]
                q[i-1] = q[i]
                q[i] = temp
                total_bribes += 1
            # If i made two swaps
            elif  i - 2 >= 0 and index == q[i-2]:
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = q[i-2]        
                total_bribes += 2
            else:
                print("Too chaotic")
                return          
                                         
    print(total_bribes)
    

if __name__ == '__main__':

        test_1 = [2, 1, 5, 3, 4]
        test_2 = [5, 1, 2, 3, 7, 8, 6, 4]
        test_3 = [1, 2, 5, 3, 7, 8, 6, 4]

        minimumBribes(test_1)
        minimumBribes(test_2)
        minimumBribes(test_3)
