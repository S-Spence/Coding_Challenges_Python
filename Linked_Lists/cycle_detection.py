"""
Problem: Given a linked list, determine if it has a cycle and return the node where the cycle begins. Return null if there is no cycle.
        Leetcode (Medium): https://leetcode.com/problems/linked-list-cycle-ii/

"""

class Node:

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
The optimal solution uses Floyd's Tortoise and Hare algorithm. FAANG comapnies expect you to know this.
"""
def optimized_find_cycle(head):
    """
    Use Floyd's Tortoise and Hare algorithm
    
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

"""Tests on Leetcode for these functions"""
