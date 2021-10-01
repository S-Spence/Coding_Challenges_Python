"""This question asked you to find the maximum profits of a pie chart when given k-contiguous sections and 
having to take every section opposite to it in a pie chart. """

"""ex: [1, 5, 1, 3, 7, -3], max profit = 16]"""

def maxProfit(arr, k):

    # Cannot make a pie chart with uneven numbers or an empty list
    if len(arr) %2 != 0 and len(arr) != 0:
        return 

    split = len(arr)//2
    max_profit = float("-inf") 
    
    
    for i in range(split-k+1):
        
        sub_arr = arr[i:i+k]
        opposites = arr[i+split:i+k+split]
        profit = sum(sub_arr + opposites)

        if max_profit and profit > max_profit:
            max_profit = profit

    return max_profit


    
    


if __name__ in "__main__":

    test_one = [1, 5, 1, 3, 7, -3] 
    test_two = []
    test_three = [0, 0, 0]
    test_four = [-10, -10, -10, -10]
    k = 2

    print(maxProfit(test_one, k))
    print(maxProfit(test_four, 4))
