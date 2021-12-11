#!/usr/bin/env python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-01-27
# Title: Max Hourglass Sum Challenge
# Description: This challenge takes input for a 2D (6X6) array and calculates the sum of all hourglass formations within the array.
#              The function then returns the maximum hour glass sum within the array.   
#              The function takes 6 input strings containing 6 integers to build the build (e.g 1 2 3 4 5 6)            
#---------------------------------------------------------------------------------------------------------------------------------------
import sys


def sum_hour_glass(arr: list) -> int:
    """ Find the sum of the hour glass formation in a 6X6 grid."""
    max_sum = -63   # Store lowest int (-9 * 7) as max int
    
    # Add hourglass values, staying in the range of a 6X6 2d array
    for i in range(4):
        for j in range(4):
            sum_hr = (arr[i][j] + arr[i][j+1] + arr[i][j + 2] + arr[i + 1][j+1] +
                     arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            
            # If hour glass sum is greater than max_sum, assign to max_sum
            if sum_hr > max_sum:
                max_sum = sum_hr
                                  
    return max_sum

              
def main() -> None:
    """Main function"""
    arr = []
    
    # Take row input and strip whitespace
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
          
    # Find max hourglass sum
    print(sum_hour_glass(arr))
    
    return


if __name__ == '__main__':
    sys.exit(main())
