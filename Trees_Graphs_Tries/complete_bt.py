"""Script from LeetCode to test Complete Binary Tree Challenge"""
import collections

class TreeNode:
     def __init__(self, value=0, left=None, right=None):
         self.value = value
         self.left = left
         self.right = right

class CBT():

    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])

        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        

    def insert(self, v):

        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.value


def level_order(root: TreeNode) -> "list[list[int]]":
    """return an array of arrays contaning the level order traversal of a BST. Runtime O(n), Space: O(n)"""
    # If the tree is empty, reurn an empty list
    if root == None:
        return []
    # initialize queue and output list
    queue = []
    output_list = []
    # append the root node to the queue
    queue.append(root)
    # Runtime O(n) becaus the while loops only touch each value once
    # output while loop to traverse tree
    while len(queue) > 0:
        length = len(queue)
        count = 0
        curr_level = []
        # inner while loop to track levels
        while count < length:
            # Remove the first node in the queue and add to current level array
            node = queue.pop(0)
            curr_level.append(node.value)
            # Increment count to track nodes added at the this level
            count += 1
            # Determine if there is a left and right child and add to the queue for the next round
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        # Append the current level list to the output list
        output_list.append(curr_level)
    # Return output list
    return output_list

    
# Test
list_1 = [7, 8, 9, 10, 11, 12, 13]
cbt = CBT(TreeNode(7))

for i in range(1, len(list_1)):
    cbt.insert(list_1[i])

print(level_order(cbt.root))
