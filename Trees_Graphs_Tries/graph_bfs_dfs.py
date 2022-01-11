import unittest
from collections import deque
"""
Problem: Traverse a graph using bfs and dfs


"""


def dfs(graph: "list[int[int]]", vertex: int, values: "list[int]", seen: dict):
    # add the vertex to output
    values.append(vertex)
    seen[vertex] = True
    # track connections
    connections = graph[vertex]
    # If the connection is unseen. recursively traverse
    for connection in connections:
        if connection not in seen:
            dfs(graph, connection, values, seen)


def graph_dfs(graph: "list[int[int]]") -> "list[int]":
    """Graph dfs traversal"""
    # Track values and seen values
    values = []
    seen = {}
    # call recursive dfs function
    dfs(graph, 0, values, seen)
    return values


def graph_bfs(adj_list: "list[int[int]]") -> "list[int]":
    """Graph bfs traversal"""
    # intiialize queue and first element to zero
    queue = deque()
    queue.append(0)
    # track values to return and seen values
    values = []
    seen = {}
    # while there are values in the queue, add to vertex list and update seen values
    while len(queue) > 0:
        vertex = queue.popleft()
        values.append(vertex)

        seen[vertex] = True
        # get the connections to the current node and append them to the queue if unseen
        connections = adj_list[vertex]

        for i in range(len(connections)):
            connection = connections[i]

            if connection not in seen:
                queue.append(connection)

    return values


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.adj_lists = [
            [
                [1, 3],
                [0],
                [3, 8],
                [0, 2, 4, 5],
                [3, 6],
                [3],
                [4, 7],
                [6],
                [2]
            ]

        ]

        self.answers = [[0, 1, 3, 2, 4, 5, 8, 6, 7],
                        [0, 1, 3, 2, 8, 4, 6, 7, 5]]

    def test_1(self):
        self.assertTrue(graph_bfs(
            self.adj_lists[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(graph_dfs(
            self.adj_lists[0]) == self.answers[1])


# Run tests
if __name__ == "__main__":
    unittest.main()
