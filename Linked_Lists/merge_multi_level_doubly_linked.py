"""
Problem: Given a doubly-linked list, list nodes also have a child property that can point to a separate doubly linked list. 
        These child lists can also have one or more child doubly linked listsof their own, and so on.
        It does not have to have a child, but it can. Flatten the linked list by merging the child levels in where they appear
        between the parent and the parent's next value.
        Leetcode: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Step 1: Constraints
        Can each level have multiple doubly linked lists? -> Yes
        What to do with child proprties after flattening? -> set the child value to null
Step 2: Tests
        1->2->3->4->5->6
          (2)-> 7->8->9 (5)->12->13
                   (8)-> 10->11       output -> 1->2->7->8->10->11->9->3->4->5->12->13->6

        1->2
        (1)->3     output -> 1->3->2

Step 3: Solution
        Determine if a node has a child
        Determine the important values to relink the list after merge
        Traverse list until end

"""
"""
Karen Fischer provided the following helper functions to test code for this problem to correspond with Leetcode test input. 
Find code here: https://replit.com/@karencfisher/doublelist#main.py
"""

class Node:
  def __init__(self, val=None, prev=None, 
                next=None, child=None):
    self.val = val
    self.next = next
    self.prev = prev
    self.child = child

null = None

def makeLists(array):
  '''
  Recursively generates the complete graph from given serialization
  Parameter:
    array - serialization of the list as Python list
  Returns:
    head to the top most list (first node of the
    graph)
  '''
  head = None
  prev = None
  i = 0
  while i < len(array):
    if array[i] != null:
      node = Node(val=array[i], prev=prev)
      if prev is None:
        head = prev = node
      else:
        prev.next = node
        prev = node
      i += 1
    else:
      node = head
      end = False
      while array[i] == null:
        if node.next is None:
          end = True
        else:
          node = node.next
        i += 1
      if end:
        node.child = makeLists(array[i:])
      else:
        node.prev.child = makeLists(array[i:])
      break
  return head

def strLists(head, lists):
  '''
  Helper function to recursively serialize the graph prior to visualization. It's an interim step and
  only meant to be called by the printLists function.

  Parameters:
    head - head of the present list 
    lists - the serialization being built recursively (passed by reference)

  Returns:
    None (lists is updated in place). 
  '''
  if head is None:
    return
  nodes = []
  while head:
    nodes.append(str(head.val))
    if head.child is not None:
      nodes.append('|')
      strLists(head.child, lists)
    head = head.next
  lists.append(nodes)

def printLists(head):
  '''
  Visualizes the entire graph
  Parameter:
    head - the top most Node
  '''
  lists = []
  strLists(head, lists)
  if lists == []:
    print(None)
    return
  previndent = 0
  for j, l in enumerate(lists[::-1]):
    count = -1
    indent = 0
    s = []
    for i in range(len(l)):
      if l[i] != '|':
        s.append(l[i])
        count += 1
      else:
        indent = count * 4
        child = count
    print('---'.join(s)) 
    if  len(lists) > 1 and j < len(lists) - 1:
      previndent += indent
      indentation = ''.join([' '] * previndent)
      if len(l[0]) > 1:
        indentation += ''.join([' '] * child)
      print(indentation + '|')
      print(indentation, end='')

def checkLinks(head, lists=None):
  '''
  Verifies that all lists can be traversed in both directions.

  Parameter:
    head - top most Node

  Returns:
    Boolean, True if all lists traversable, False if not.
  '''
  if head is None:
    return True
  if lists is None:
    lists = []
  stack = []
  result = True
  node = head
  while node is not None:
    if node.child is not None:
      checkLinks(node.child, lists)
    stack.append(node)
    prev = node
    node = node.next
  while prev is not None:
    if len(stack) == 0 or stack.pop() != prev:
      result = False
    prev = prev.prev
  lists.append(result)
  return all(lists)

"""
The challenge function is below. Worst case runtime: O(n)
"""
def flatten(head: Node) -> Node:
    """Flatten the multi-level linked lists"""
    # Return head if the list is empty
    if head is None:
        return head
    # Set current to head
    current = head
    # While current is not the tail, determine if current has a child
    while current != None:
        # If no child, move current, else determine the tail of the merging list
        if current.child == None:
            current = current.next
        else:
            # Find the tail of nested list
            tail = current.child
            while tail.next != None:
                tail = tail.next
            # Link the tail to current's next value both ways
            tail.next = current.next
            if tail.next != None:
                tail.next.prev = tail
            # Link the list infront 
            current.next = current.child
            current.next.prev = current
            # Now there is no child since the list has been merged
            current.child = None
    return head

def print_list(head):
    """Print the linked list"""
    # set the value to print as the head node
    print_val = head
    # Loop until hitting the tail of the linked list
    while print_val is not None:
        print(f"{print_val.val}->", end="")
        print_val = print_val.next
    print("Null")


# Test one
array = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
head = makeLists(array)
print("Input")
print("--------------------------------------------")
printLists(head)
print("Output")
print("--------------------------------------------")
l1 = flatten(head)
print_list(l1)
print()
print("Expected")
print("--------------------------------------------")
print("1->2->3->7->8->11->12->9->10->4->5->6->Null")
print()

# Test two
array = [1,2,null,3]
head = makeLists(array)
print("Input")
print("--------------------------------------------")
printLists(head)
print("Output")
print("--------------------------------------------")
l2 = flatten(head)
print_list(l2)
print()
print("Expected")
print("--------------------------------------------")
print("1->3->2-Null")
print()
