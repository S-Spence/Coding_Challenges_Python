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
Step 3: Solution -> use the same technique as reversed linked list, but 
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

    # TODO: handle the case of the whole list reversing
    def reverse_m_to_n(self, m, n):
        """
        Reverse the vallues in a linked list from position n to position m.
        Space complexity: O(1), time complexity O(n).
        """
        # If the list is empty, return None
        if self.head == None:
            return None
        "Test: 1->2->3->4->5 return 5->4->3->2->1"
        current = self.head # 1
        position = 1
        start = self.head # 1
        # 1 -> 2 
        while position < m: 
            start = current # 1
            current = current.next # 2
            position += 1 # 2

        new_list = None
        tail = current # 2
        # 2 -> 3 -> 4 -> 5
        while position >= m and position <= n: 
            next = current.next  # 3 -> 4 -> 5
            # Reverse the elements between m and n
            current.next = new_list # None -> 2 -> 3
            new_list = current # 2 -> 3 -> 4
            # Update the current value and loop variable
            current = next # 3 -> 4 -> 5
            position += 1 # 3 -> 4 -> 5
        # Reconnect the linked list
        start.next = new_list # start = 1, so 1 connects to 4
        tail.next = current # 5 tail equals 2, so 2 connects to 5
        # If m is less than one, then return the new list, else return the head of the list
        if m > 1:
            return self.head
        else:
            return new_list.val
    
# Test 1: 1->2->3->4->5 return 1->4->3->2->5
test1 = LinkedList()

for i in range(5):
    test1.insert_end(i+1)

print("Original Linked List")
print("--------------------")
test1.print_list()
m = 2
n = 4
print(f"Reversed Linked List {m}-{n}")
print("--------------------")
test1.reverse_m_to_n(m, n)
test1.print_list()

m = 1
n = 5
print(f"Reversed Linked List {m}-{n}")
print("--------------------")
test1.reverse_m_to_n(m, n)
test1.print_list()

# Test 2: 3->Null
test2 = LinkedList()
test2.insert_front(3)
print("Original Linked List")
print("--------------------")
test2.print_list()
m = 1
n = 1
print(f"Reversed Linked List {m}-{n}")
print("--------------------")
test2.reverse_m_to_n(m, n)
test2.print_list()

# Test 3 null
test3 = LinkedList()
print("Original Linked List")
print("--------------------")
test3.print_list()
m = 0
n = 0
print(f"Reversed Linked List {m}-{n}")
print("--------------------")
test3.reverse_m_to_n(m, n)
test3.print_list()
