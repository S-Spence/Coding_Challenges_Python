import unittest
from collections import deque
"""
Problem: There are a total of n courses to take labeled from 0 to n-1. Some courses have pre-requisite courses. This is expressed as 
        a pair i.e [1, 0] which indicates you must take course 0 before course 1. Given the total number of courses,
        and an array of prerequisite pairs, return if it is possible to finish all courses. 

        Leetcode: https://leetcode.com/problems/course-schedule/ 

Constraints: 
        Can we have courses unconnected to the other courses? -> Yes
        What to return if there are no prereqs? -> True
Tests:
    2, [[1, 0], [0, 1]] -> false
    6, [[1,0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]] -> true
    2, [[0, 1]] - > true

Solution: A cycle would prevent the algorithm from being able to finish the courses. 
        Use a directed graph (adj list) to represent the index (course) mapped to its prereqs.
        courses = 6 pre_reqs = [[1,0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
        0: [1]
        1: [2]
        2: []
        3: [0, 4]
        4: []
        5: [2, 3, 4]

        The questions is essentially asking you to determine if the graph is cyclic or acyclic
        

"""

"""
BFS solution
"""
def course_schedule(num_courses: int, pre_reqs: "list[int]") -> bool:
    """
    Determine if it is possible to finish all courses given a list of prerequisites
    Runtime(p + n^3), Space: O(n^2)
    """
    # Return true if there are no prereqs
    if len(pre_reqs) == 0:
        return True
    # Initialize graph, time: O(n)
    dir_graph = [[] for i in range(num_courses)]

    # Fill graph mapping courses to their prereqs, time: O(p) where p is the number of pairs, space: O(n^2)
    for val in pre_reqs:
        dir_graph[val[1]].append(val[0])
    # Time O(n)
    for vertex in range(num_courses):
        # Initialize queue
        queue = deque()
        seen = {}
        # Add all current class prereqs to the queue. Worst case time: O(n)
        for i in range(len(dir_graph[vertex])):
            queue.append(dir_graph[vertex][i])

        # Perform bfs Time: O(n), Space: O(n)
        while len(queue) > 0:
            current = queue.popleft()
            seen[current] = True

            # check for cycle
            if current == vertex:
                return False

            adjacent = dir_graph[current]
            # add unseen values to the queue worst case: O(n)
            for i in range(len(adjacent)):
                next = adjacent[i]

                if next not in seen:
                    queue.append(next)
    return True


"""
Topological Sort Solution. Topological sort returns a certain order of the vertices of a given graph.

Notes: Every verex in isolation has what is known as an Indegree factor. This only applies if the index is within a
       directed graph. The indegree value is represented as how many connections are coming into the vertex.
       Represent the node in terms of their indegree value.
       You can only take a vertex and its value if its indegree value is zero. Once you take it, you must remove it
       from the graph and reduce the indegree value of any nodes that it was directing into. 
       You can take the values with a 0 indegree in any order.
       Think of the indegree 0 values as the vertices with no dependencies.
       Topological sort is applicable in DAGs (Directed Acyclic Graphs). This means the graph may not contain cycles.
"""
def course_schedule_topological(num_courses: int, pre_reqs: "list[int]") -> bool:
    """
    Use topological sort to determine if it is possible to complete all courses
    runtime: O(p + n^2), space: O(n^2) 
    """
    # Return true if there are no prereqs
    if len(pre_reqs) == 0:
        return True
    # Initialize graph, time: O(n)
    dir_graph = [[] for i in range(num_courses)]
    in_degrees = [0 for i in range(num_courses)]

    # Fill graph mapping courses to their prereqs, time: O(p) where p is the number of pairs, space: O(n^2)
    # Also fill in degree array: time: O(p), Space: O(n^2)
    for val in pre_reqs:
        dir_graph[val[1]].append(val[0])
        in_degrees[val[0]] += 1
    # Initialize a stack to track the courses with no pre-reqs or met pre-reqs
    stack = []
    # Add values to stack if they can be removed
    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            stack.append(i)
    # Initialize a count
    count = 0
    # While there are classes with no prereqs, increment the count and remove the value from the stack
    while len(stack) > 0:
        current = stack.pop()
        count += 1
        # Get the prereqs of the current course
        adjacent = dir_graph[current]
        # Decrement the in_degree for the courses with dependencies
        for i in range(len(adjacent)):
            next = adjacent[i]
            in_degrees[next] -= 1
            # If the value has no dependencies, add to stack
            if in_degrees[next] == 0:
                stack.append(next)

    return count == num_courses


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.pre_reqs = [
            [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]],
            [[1, 0], [0, 1]],
            [[1, 0]]
        ]

        self.num_courses = [6, 2, 2]

        self.answers = [True, False, True]

    def test_1(self):
        self.assertTrue(course_schedule(
            self.num_courses[0], self.pre_reqs[0]) == self.answers[0])

    def test_2(self):
        self.assertTrue(course_schedule(
            self.num_courses[1], self.pre_reqs[1]) == self.answers[1])

    def test_3(self):
        self.assertTrue(course_schedule(
            self.num_courses[2], self.pre_reqs[2]) == self.answers[2])

    def test_4(self):
        self.assertTrue(course_schedule(
            self.num_courses[0], self.pre_reqs[0]) == self.answers[0])

    def test_5(self):
        self.assertTrue(course_schedule(
            self.num_courses[1], self.pre_reqs[1]) == self.answers[1])

    def test_6(self):
        self.assertTrue(course_schedule(
            self.num_courses[2], self.pre_reqs[2]) == self.answers[2])


# Run tests
if __name__ == "__main__":
    unittest.main()
