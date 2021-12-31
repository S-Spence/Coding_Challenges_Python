"""
Problem: Given two linked lists storing digits, retrun the sum of the linked lists as a linked list 

        Ex. 2->4->3
            5->6->4
            -------
            8->0->7
        Leetcode: https://leetcode.com/problems/add-two-numbers-ii/
Constraints:
        What to return if the list is empty? -> Assume the list will not be empty

Tests: 
    l1 = 2->4->3, l2 = 5->6->4 ->  243 + 564 = 807 = result = 8->0->7
    l1 = 9->0->3, l2 = 2 ->0->0 -> = 903 + 200 = 1103 + result = 1->1->0->3
    l1 = 0, l2 = 0 -> reult = 0

Solution: Reverse the linked lists to apply the same logic from add_two_numbers.py and add from the ends, carrying the remainder.
          Also reverse the output so it is in the correct order.
          Runtime: O(m + n), Space: O(m + n) 
"""
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def reverse(head: ListNode) -> ListNode:
        """Helper function to reverse linked lists"""
        current = head
        prev = None
        
        while current:
            
            next = current.next
            current.next = prev
            prev= current
            current = next
        
        head = prev
        return head
        
def add_numbers_II(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Given two linked lists, add the numbers and return the result in a linked list
    Runtime: O(m + n), soace O(m + n)
    """ 
    result = ListNode()   # results list
    current = result       # track current node
    carry = 0              # carry remainder > 10

    # Reverse the linked lists  
    l1 = reverse(l1)
    l2 = reverse(l2)
        
    while l1 or l2 or carry:
            
        # Initialize to zero for total calculation
        val_1 = 0
        val_2 = 0
        # Update values if they exist and shift pointers
        if l1:
            val_1 = l1.val
            l1 = l1.next
        if l2:
            val_2 = l2.val
            l2 = l2.next
        # Calculate total
        total = val_1 + val_2 + carry
        # Set current node and carry  
        current.next = ListNode(total%10)
        carry = total//10
        # Move pointer
        current = current.next
    # Reverse the output so it is in the correct order  
    return reverse(result.next)




# Create L1 elements
l1_1 = ListNode(2)
l1_1.next = ListNode(4)
l1_1.next.next = ListNode(3)

l1_2 = ListNode(9)
l1_2.next = ListNode(0)
l1_2.next.next = ListNode(3)

l1_3 = ListNode(0)

# Create L2 elements
l2_1 = ListNode(5)
l2_1.next = ListNode(6)
l2_1.next.next = ListNode(4)

l2_2 = ListNode(2)
l2_2.next = ListNode(0)
l2_2.next.next = ListNode(0)

l2_3 = ListNode(0)

# Get results
l3_1 = add_numbers_II(l1_1, l2_1)
l3_2 = add_numbers_II(l1_2, l2_2)
l3_3 = add_numbers_II(l1_3, l2_3)

results = [l3_1, l3_2, l3_3]
expected = ["807", "1103", "0"]

for i in range(len(results)):
    print(f"Expected: {expected[i]}")
    while results[i]:
        print(results[i].val, end="")
        results[i] = results[i].next
    print("")
    
            