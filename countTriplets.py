#!/usr/bin/env python
import random

def countTriplets(arr, r):
    """Count triplets appearing in progressing order in multiples of r"""
    count = 0
    before = dict()
    after = dict()
    
    # Add all elements to the after dictionary
    for val in arr:
        if val in after.keys():
            after[val] += 1
        else: 
            after[val] = 1
    
    """ Iterate through the array, removing the current element from the after list.
        Increase the count if the current value is divisble by r, the current value
        divided by r is in the before dictionary, and the current value multiplied by r is
        in the after dictionary. Finally, move the current element to before dictionary. """
    for val in arr:
        # Remove the element from the after dictionary
        after[val] -= 1
        # If val is divisible by r, val//r in before dict, and val*r in after dict,
        # increase count by the number of matching elements in the before dict * the
        # number of matching elements in the after dict. 
        if val %r == 0 and val//r in before.keys() and val * r in after.keys():
            count += before[val//r] * after[val*r]
        
        # Move the current element to the before dictionary
        if val in before.keys():
            before[val] += 1
        else:
            before[val] = 1  
    
    return count
                                                  
if __name__ == '__main__':

    # Generate some test data
    test_1 = [1, 5, 5, 25, 125]
    test_2 = [1, 3, 9, 9, 27, 81]
    test_3 = [1 for i in range(100)]
    test_4 = [random.randint(0, 10000) for i in range(1000)]
    

    # Test the above samples and add to a list to format output
    ans1 = countTriplets(test_1, 5)
    ans2 = countTriplets(test_2, 3)
    ans3 = countTriplets(test_3, 1)
    ans4 = countTriplets(test_4, 4)
    answers = [ans1, ans2, ans3, ans4]

    # Print output
    for val in range(len(answers)):
        print(f"Test {val + 1}: {answers[val]} triplets")

