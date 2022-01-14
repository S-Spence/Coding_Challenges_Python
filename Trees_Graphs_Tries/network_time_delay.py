import unittest
import math
import heapq

"""
Problem: There are n network nodes labelled 1 to N. Given a times array,
        containing edges represented by arrays [u, v, w] where u is the source node,
        v is the target node, and w is the time taken to travel from the source node to
        the target node.
        Send a signal from node k, return how long it takes for all nodes to recieve
        the signal. Return -1 if it is impossible.
        Leetcode: https://leetcode.com/problems/network-delay-time/
Constraints: 
    Can the graph be unconnected? -> Yes, if so return -1
    Can there be negative wieghts for edges? -> No
    Follow-up ->  YES... use Bellman-Ford

Tests:
    input: n = 5, k = 1, times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
    output = 14

    input: n = 3, k = 1, times = [[2, 3, 4]]
    output: -1

    input: n = 3, k = 1, times = [[1, 2, 8], [3, 1, 3]]
    ouput = -1

Note: This is a directed and weighted graph. When you are looking for the shortest path to any node from all other nodes, 
the following two algorithms will apply with directed, weighted graphs.

Solution 1: Dijkstra's Algorithm. Pronounced (dike-stra's algorithm)
        This is an algorithm specifically taylored to solve this type of graph problem. You must understand the greedy method to
        understand Dijkstra's algorithm. This algorithm only applied to direct, weighted graphs to determine the shorted distance from
        node x to every other node. 

        Greedy Method: An algorithmis paradigm that only applied to optimization problems. These are problems when you are looking
        for max or min possible value. Greedy algorithms choose the optimal answer at each step.

        Dijkstra's Algorithm takes the shortest path without ever traversing back to that vertex.
        Every value in the graph should be mapped as the distance from the starting verex to that vertex
        
        The graph initializes with all vlaues set to infinity

        Step 1: initialize the directed, weighted graph. 
        Step 2: use the times array, you do not need to build an adjacency array for this algorithm
        Step 3: close off the current node so we do not traverse back to it
        Step 4: take the vertex with the lowest weight in the graph and redo step 2 until all nodes are complete
        Step 5: Only update the final vertex if the current value will be less
        Step 6: The maximum value inside the array will be the shortest path in the network

        Note: If you ever get back infinity, return -1 because there is an unreachable vertex.

Solution 2: Bellman-Ford Algorithm
    The Bellman-Ford algorithm is used when you must solve optimization problems with a directed graph with negative weights
    included. 
    The Bellman-Ford algorithm relies on dynmaic programming.

    You must explore the edges n-1 times. Bellman-Ford aims to save some of these computations with memoization. 
    You memoize the values of the shortest traversal paths for each node.

    The algorithm finds the lowest possible path to each node and does not recalculate the path if it has found the shortest.
    If the target is less than the target weight, update value of shortest path for that node. 
    Look at every vertex/weight pair 
        --IE. (1, 3): This explores node 1 to 3. You add the weight to the current value at one.
        --Only update 3 if the weight calculated is less than the current weight at 3.
    You must run through this for every vertex/weight pair in the list, then perform this iteration n-1 times to ensure you find
    the lowest possible path.
    You can finish before the nth-1 iteration if you ever run through an iteration and nothing changes in the distances array. 
   

    Step 1: fill a structure with infinty to represent shortest distances to each node.
    Step 2: fill the graph structure with vertex: target, weight pairs.
    Step 3: Loop through every vertex in the graph. Add the source node's value and the weight to get to its target for that 
    graph value. Update the value at the target node in the distances array if this calculation is less than the current value.
    Step 4: Repeat step 3 n-1 times. Break if you ever perform an iteration without making any updates.
    
    Constraint: 
    The Bellman-Ford algorithm does not work if there is a negative cycle. To detect a negative cycle, go up to n-1 iterations. Then,
    perform the nth iteration. If any values update on the nth iteration, there is a negative cycle. 
    
"""


def dijkstras_network_delay(n: int, k: int, times: "list[int]") -> int:
    """
    Dijkstra's algorithm to determine network time delay.
    Runtime: O(E * logn) where E is the number of edges and n is the number of vertices, Space: O(E + N)
    The time complexity is O(E logn) because it drop the nlogn from the calculation because E will always be greater than N
    """
    # Fill the distances array for Dijkstra's algorithm
    distances = [math.inf for i in range(n)]
    # Initialize the adjacency array for the graph
    graph = [[] for i in range(len(distances))]
    # set the starting node equal to zero in distance
    distances[k-1] = 0
    # Initialize a min heap and add the starting vertex
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, k-1)

    # Fill the graph
    for i in range(len(times)):
        source = times[i][0]
        target = times[i][1]
        weight = times[i][2]
        # append the target node and its weight to the source node's reachable nodes
        graph[source-1].append([target-1, weight])

    # While there are values in the heap, perform the steps described above in the notes for Dijkstra's algorithm
    while len(heap) > 0:
        # Pop the current value from the heap and retrive the nodes it can reach
        current_vertex = heapq.heappop(heap)
        adjacent = graph[current_vertex]
        """ If the weight of the current verex is less than the weight of the neighboring vertex, update the neighbor vertex and add
            it to the queue"""
        for i in range(len(adjacent)):
            neighbor_vertex = adjacent[i][0]
            weight = adjacent[i][1]
            if distances[current_vertex] + weight < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distances[current_vertex] + weight
                heapq.heappush(heap, neighbor_vertex)
    # Return the maximum distance in the distance array because this is the time to traverse all vertices
    answer = max(distances)
    # If there was an unreachable vertex, return -1
    if answer == math.inf:
        return -1

    return answer


def BF_network_time_delay(n: int, k: int, times: "list[int]") -> int:
    """
    Use the Bellman-Ford Algorithm to determine network time delays for graph with negative weights.
    Runtime: O(n*e) where n is the vertices and e are the edges (weights). Space: O(n).
    Note: Dijkstra's algorithm is a faster algorithm. However, it cannot handle negative weights. 
    """
    # Fill the distances array for Bellman-Ford algorithm
    distances = [math.inf for i in range(n)]
    # set the starting node equal to zero in distances
    distances[k-1] = 0

    # Perform the updates to the distances array n-1 times
    for i in range(n-1):
        # Track changes for this iteration
        changes = 0
        # Loop through every values in the times array and update shortest path and changes made as needed
        for j in range(len(times)):
            source = times[j][0]-1
            target = times[j][1]-1
            weight = times[j][2]

            if distances[target] > distances[source] + weight:
                distances[target] = distances[source] + weight
                changes += 1
        # If there were not changes in this iteration, stop the algorithm
        if changes == 0:
            break
    # Return the maximum value in the distances array because this is the shortest path. Return -1 if a vertex was unreachable.
    ans = max(distances)

    if ans == math.inf:
        return -1

    return ans


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.times = [
            [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [
                4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]],
            [[2, 3, 4]],
            [[1, 2, 8], [3, 1, 3]],
            [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3],
                [4, 5, 6], [5, 3, 7], [3, 2, 3], [3, 1, 5]]
        ]

        self.n = [5, 3, 3, 5]
        self.k = [1, 1, 1, 1]

        self.answers = [14, -1, -1, 2]

    def test_1(self):
        self.assertTrue(dijkstras_network_delay(
            self.n[0], self.k[0], self.times[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(dijkstras_network_delay(
            self.n[1], self.k[1], self.times[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(dijkstras_network_delay(
            self.n[2], self.k[2], self.times[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(BF_network_time_delay(
            self.n[0], self.k[0], self.times[0]) == self.answers[0])

    def test_5(self):
        self.assertTrue(BF_network_time_delay(
            self.n[1], self.k[1], self.times[1]) == self.answers[1])

    def test_6(self):
        self.assertTrue(BF_network_time_delay(
            self.n[2], self.k[2], self.times[2]) == self.answers[2])
    # Extra test with negative weights for Bellman-Ford

    def test_7(self):
        self.assertTrue(BF_network_time_delay(
            self.n[3], self.k[3], self.times[3]) == self.answers[3])


# Run tests
if __name__ == "__main__":
    unittest.main()
