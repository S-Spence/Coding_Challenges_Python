"""
Problem: Given a linked list and number m to n, return a linked list with only the values m-n reversed.

Step 1: Verfiy constraints
        Will m and n always be within the range of the linked list? -> yes, assume 1 <= m <= n <= length list
        Is it possible to recieve m and n as the full linked list
Step 2: Tests
        1) 1->2->3->4->5, m = 2, n = 4 return 1->4->3->2->5
        2) 1->2->3->4->5, m= 1, n = 5 return 5->4->3->2->1
        3) 5->None, m = 1, n = 1 return 5
        4) None, m=0, n=0 return None
Step 3: Solution
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

        while(current != None): # 1 -> 2 -> 3 -> 4 -> 5
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
        

# Test 1: 1->2->3->4->5
test1 = LinkedList()

for i in range(5):
    test1.insert_end(i+1)

print("Original Linked List")
print("--------------------")
test1.print_list()
print("Reversed Linked List")
print("--------------------")
test1.reverse()
test1.print_list()

# Test 2: 3->Null
test2 = LinkedList()
test2.insert_front(3)
print("Original Linked List")
print("--------------------")
test2.print_list()
print("Reversed Linked List")
print("--------------------")
test2.reverse()
test2.print_list()

# Test 3 null
test3 = LinkedList()
print("Original Linked List")
print("--------------------")
test3.print_list()
print("Reversed Linked List")
print("--------------------")
test3.reverse()
test3.print_list()
