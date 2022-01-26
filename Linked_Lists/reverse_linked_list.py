import unittest
"""
Problem (easy): Given a linked list, return it in reverse. 
Leetcode: https://leetcode.com/problems/reverse-linked-list

Step 1: Verify constraints
        What do we return if we get null or a single node as the linked list? -> retunr null or the node back
Step 2: Tests
        1->2->3->4->5 return 5->4->3->2->1
        3 return 3
        null return null
Step 3: Solution -> keep track of previous node while iterating. Update pointers.
                    Set prev node to current node and current.next to prev on each iteration using temp variable of next.
Step 4: Code -> Solution: O(n) time complexity, O(1) space.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None):
         self.val = val
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        """Insert at the head of the list"""
        # Create new node with data
        new_node = ListNode(data)
        # Meake the current head the next value
        new_node.next = self.head
        # Set new node as head node
        self.head = new_node

    def insert_end(self, data):
        """Insert at end"""
        # create new node
        new_node = ListNode(data)
        # If the Linked List is empty, set the new node as head
        if self.head is None:
            self.head = new_node
            return
        # Else find the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # Set the new node as the last node's next val
        last.next =  new_node

    def print_list(self):
        """Print the linked list"""
        # set the value to print as the head node
        print_val = self.head
        # Loop until hitting the tail of the linked list
        while print_val is not None:
            print(f"{print_val.val}->", end="")
            print_val = print_val.next
        print("Null\n")

    def reverse(self):
        """Defined outside to head node as list input for leetcode tests"""
        "Test: 1->2->3->4->5 return 5->4->3->2->1"
        prev = None 
        current = self.head # 1

        while current != None: # 1 -> 2 -> 3 -> 4 -> 5
            next = current.next # 2 -> 3 -> 4 -> 5 -> None
            # The reversal is happening here. At each value of prev (set to current), current.next shows the reversed list
            current.next = prev # None -> 1 -> 2 -> 3 -> 4
            prev = current # 1 -> 2 -> 3 -> 4 -> 5
            # This updates the loop variable
            current = next # 2 -> 3 -> 4 -> 5 -> None
        self.head = prev
 

def reverse(head):
    """Defined again outside of class to take head node as list input for leetcode tests. This only returns new head node."""
    prev = None
    current = head

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
        

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.test1 = LinkedList()

        for i in range(5):
            self.test1.insert_end(i+1)
        
        self.test2 = LinkedList()
        self.test2.insert_front(3)
        
        self.test3 = LinkedList()

    # Tests for linked lists
    def test_1(self):
        result = self.test1.reverse()
        #result = self.test1.head
        expected = "54321"
        i = 0
        while result != None:

            self.assertTrue((result.val) == int(expected[i]))
            i += 1
            result = result.next

    def test_2(self):
        self.test2.reverse()
        self.assertTrue(self.test2.head.val == 3)

    def test_3(self):
        self.test3.reverse()
        self.assertTrue(self.test3.head == None)

# Run tests
if __name__ == "__main__":
    unittest.main()
