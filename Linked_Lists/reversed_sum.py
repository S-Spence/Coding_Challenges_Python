
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None):
         self.val = val
         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Take two linked lists in reverse order and add the numbers together. Return 
    a linked list also in reverse order.
    """
    result = ListNode() # create return linked list
    copy = result       # Create a copy of the linked list to work with
    carry = 0           # Carry value for sum >= 10
    
    # While there are numbers to add
    while l1 or l2 or carry:
        
        # If linked list one has a value, move pointers
        if l1:
            v1, l1 = l1.val, l1.next
        else:
            v1, l1 = 0, None
        # If linked list two has a value, move pointers
        if l2:
            v2, l2 = l2.val, l2.next
        else:
            v2, l2 = 0, None

        # Add total
        total = carry + v1 + v2
        # Add value less than ten in copy.next
        copy.next = ListNode(total % 10)
        # Carry the rest over for the next iteration
        carry = total // 10
        # Move pointer
        copy = copy.next
    
    return result.next
 
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = addTwoNumbers(l1, l2)

while l3:
    print(l3.val, end="")
    l3 = l3.next
