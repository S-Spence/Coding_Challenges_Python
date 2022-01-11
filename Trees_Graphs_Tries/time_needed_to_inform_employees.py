import unittest

"""
Problem: A company has n employees with unique IDs from 0 to n-1. The head of the company has the idea headID. 

    You will recieve a manager's array where managers[i] is the id of the manager for employee i. 
    Each employee has one direct manager.
    The company head has no manager managers[head] = -1
    It is guaranteed that subordination relationships will have a tree structure.

    The head of the company wants to inform all employees of the news. He will inform his direct submirdinates,
    who will inform their direct subordinates, and so on until everyone knows the news. 

    You will also recieve an infrom time array where inform_time[i] is the time it takes to inform employee i to inform all
    of thier direct subordinates. 

    Return the total number of minutes it takes to inform all employees of the news

    Leetcode: https://leetcode.com/problems/time-needed-to-inform-all-employees/ 
Constraints:
    Cyclic? -> are their possible cycles in the graph? -> Yes
    Can employees have more than one manager? -> No
    Is the graph unconnected? -> No
    Does every employees have a manager? -> Yes, aside from the head of the company
    Is the graph directed? -> yes


Test:   
    Input: n = 8, headId = 4, managers = [2, 2, 4, 6, -1, 4, 4, 5] time = [0, 0, 4, 0 ,7, 3, 6, 0]
    Output: 13

    Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
    Output: 1

    Input: n = 1 head = 0 managers = [-1] inform_time = [0]

Solution:
    You must transform the input into an adjacency list first
    Use dfs to determine the maximum time to inform all subordinates of a current employee.

Notes: With graphs, BFS and DFs both yield O(n) space and time.
       Graph problems are difficult to detect as you will usually need to identify where a graph would be useful and build it
       using either a an adjacency array or and adjacency matrix depending on your problem.

"""

def dfs(curr_id: int, graph: "list[int[int]]", inform_time: "list[int]"):
    """
    Use dfs to determine the time to inform all subordinates of current employee
    Runtime: O(n), Space: O(n)
    """
    # If there are no subordinates, return 0
    if len(graph[curr_id]) == 0:
        return 0
    # Keep track of maximum minutes to inform and current subordinates
    maximum = 0
    subordinates = graph[curr_id]
    # determine if the max time is greater than the max time to inform subordinate i
    for i in range(len(subordinates)):
        maximum = max(maximum, dfs(subordinates[i], graph, inform_time))
    # Return the max time to inform + the inform time for the current employee
    return maximum + inform_time[curr_id]


    
def time_to_inform(managers: "list[int]", inform_time: "list[int]", n: int, head: int):
    """Return the time to inform all employees. Runtime: O(n), Space: O(n)"""
    # If there are no employees, return 0
    if n == 0:
        return 0
    # Initialize the graph as an adjacency array
    graph = [[] for i in range(n)]
    # Fill adjacency array
    for employee in range(n):
        manager = managers[employee]
        # skip if these is no manager (head of list)
        if manager == -1:
            continue
        # Add the employees to the manager's subordinates
        graph[manager].append(employee)
        # Call recursive dfs to determine minutes
    return dfs(head, graph, inform_time)
    
    
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.managers = [
            [2, 2, 4, 6, -1, 4, 4, 5],
            [2, 2, -1, 2, 2, 2],
            [-1]
        ]
        self.inform_times = [[0, 0, 4, 0, 7, 3, 6, 0], [0, 0, 1, 0, 0, 0], [0]] 
        self.head = [4, 2, 0]
        self.n = [8, 6, 1]
        
        self.answers = [13, 1, 0]

    def test_1(self):
        self.assertTrue(time_to_inform(
            self.managers[0], self.inform_times[0], self.n[0], self.head[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(time_to_inform(
            self.managers[1], self.inform_times[1], self.n[1], self.head[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(time_to_inform(
            self.managers[2], self.inform_times[2], self.n[2], self.head[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
