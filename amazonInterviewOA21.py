"""This question asked you to find the maximum profits of a pie chart when given k-contiguous sections and 
having to take every section opposite to it in a pie chart. """

"""ex: [1, 5, 1, 3, 7, -3], max profit = 16]"""

def maxProfit(arr, k):

    split = len(arr)//2
    max_profit = -100000
    for i in range(0, split):
        
        sum = 0
        sub_arr = arr[i:i+k]
        print(sub_arr)
      
        """for j in range(0, k):
            sum += arr[j] + arr[j+split]
        if sum > max_profit:
            max_profit = sum"""


    
    return max_profit


for __name__ in "__main__":

    test_one = [1, 5, 1, 3, 7, -3] 
    k = 2

    print(maxProfit(test_one, k))
