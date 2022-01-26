import unittest
"""
Problem: Given a linked list, determine if it has a cycle and return the node where the cycle begins. Return null if there is no cycle.
        Leetcode (Medium): https://leetcode.com/problems/linked-list-cycle-ii/

Tests: See tests on leetcode

Solutions: 
        Brute Force: Use a set to track seen nodes. A set has O(1) lookup. Runtime: O(n), Space: O(n)
        Floyd's Tortoise and Hare: Runtime O(n), Space O(1)
"""

class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


def find_cycle(head):
    """
    Determine if a linked list has a cycle and return the node that begins the cycle.
    Time: O(n), space: O(n)
    """
    # set the head to the current node
    current = head
    # Use a set to keep track of seen nodes
    seen_nodes = set()
    # While the current node is not in the set, determine if there is a tail. Set has O(1) lookup.
    while current not in seen_nodes:
        # Does the list end? 
        if current.next == None:
            return None
        # If not, add the current node to seen nodes and update current node
        seen_nodes.add(current)
        current = current.next

    return current


"""
Note: the optimal solution uses Floyd's Tortoise and Hare algorithm. FAANG comapanies expect you to know this.
"""
def optimized_find_cycle(head):
    """
    Use Floyd's Tortoise and Hare algorithm. Runtime O(n), Space O(1)
    
    """
    # Return None if the list is empty
    if head == None:
        return None
    # Initialize to the same value at first
    tortoise = head
    hare = head
    # While the hare and tortiose have a next node
    while True:
        hare = hare.next
        tortoise = tortoise.next
        # Advance the hare two steps to the tortoise's one
        if hare == None or hare.next == None:
            return None
        else:
            hare = hare.next
        # break if the tortoise and hare are pointing to the meeting point list node
        if tortoise == hare:
            break
    # Determine where the cycle begins by finding where the pointers meet
    p1 = head
    p2 = tortoise
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    
    return p1

class TestMethods(unittest.TestCase):
    def setUp(self):
        # Create list with cycle
        self.l1 = ListNode(3)
        self.l1.next = ListNode(2)
        self.l1.next.next = ListNode(0)
        self.l1.next.next.next = ListNode(4)
        # create cycle
        self.l1.next.next.next.next = self.l1.next

        # Create list without cycle
        self.l2 = ListNode(3)
        self.l2.next = ListNode(2)
        self.l2.next.next = ListNode(0)
        self.l2.next.next.next = ListNode(4)
        

    # Tests solution one
    def test_1(self):
        self.assertTrue(find_cycle(self.l1).val == 2)

    def test_2(self):
        self.assertTrue(find_cycle(self.l2) == None)

    # Tests solution two
    def test_3(self):
        self.assertTrue(optimized_find_cycle(self.l1).val == 2)

    def test_4(self):
        self.assertTrue(optimized_find_cycle(self.l2) == None)


# Run tests
if __name__ == "__main__":
    unittest.main()
