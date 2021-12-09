#!/usr/bin/env python
"""Count the longest increasing sub array for a given array. The numbers must be consecutive"""

def number_of_longest_increasing_sub_arrays(a: list)-> int:
    """A function to count the number of longest increasing sub arrays"""
    current_length = 1          # Current length
    length_longest = 1          # Longest length
    count_longest = 1           # Count of longest sub arrays

    # Loop through the values in the array
    for i in range(0, len(a)-1):
        # if the values are in increasing order, increase current length. Else, reset to 1
        if a[i] < a[i+1]: 
            current_length += 1
        else:
            current_length = 1

        # If the current length is the longest sub array, set to longest length and reset the count to one
        if current_length > length_longest:
            length_longest = current_length
            count_longest = 1
        # If the current length is equal to the longest sub array, increase the count
        elif current_length == length_longest:
            count_longest += 1
    return count_longest


def main():
    # Test cases
    array_1 = [1,3,4,2,7,5,6,9,8]
    print(number_of_longest_increasing_sub_arrays(array_1))

if __name__ == "__main__":
    main()

