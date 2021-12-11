import random

class BST:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
       

    def insert(self, val):
        
        if val == self.data:
            return

        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)
            
            
    def in_order_traversal(self):
        """In order traversal recursivly traverses the tree by left, root, right. In order prints BST in sorted order (DFS algorithm)"""
        elements = []
        if self.left:
            # += instead of append copies all elements of right side list into left side list instead of .append() for one val
            elements += self.left.in_order_traversal()
            #self.left.in_order_traversal()
        elements.append(self.data)
        #print(self.node)
        if self.right:
            elements += self.right.in_order_traversal()
            #self.right.in_order_traversal()
        return elements
    
    """Pre-order traversal recusively traverses the tree by root, left, right (DFS algorithm)"""
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements

    """Post-order traversal recusively traverses the tree by left, right, root. This method is good for deletion"""
    def post_order_traversal(self):
        elements = []

        if self.left:
            # += instead of append copies all elements of right side list into left side list instead of .append() for one val
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        
        return elements
    """TODO: FIX function
    def breadth_first_search(self, root):
     
        # Create an empty queue
        # for level order traversal
        queue = []
 
        # Enqueue Root and initialize height
        queue.append(root)
        output = []
        while(len(queue) > 0):
       
            # Print front of queue and
            # remove it from queue
            output.append(queue[0])
            node = queue.pop(0)

            if node is None:
                continue
            #Enqueue left child
            if node.left is not None:
                queue.append(node.left)
 
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
        return output
    """
    def get_height(self, node):
        """Print the height of the BST"""
        if node is None:
            return -1

        return 1 + max(self.get_height(node.left), self.get_height(node.right))




if __name__ == "__main__":
    numbers_2 = [5, 6, 4, 3, 2, 56, 45, 32, 17, 89, 92, 50]
    numbers = [3, 5, 2, 14, 6, 7]
    tree = BST(numbers[0])
    tree2 = BST(numbers_2[0])

    for i in range(1, len(numbers)):
        tree.insert(numbers[i])
    
    #for i in range(1, len(numbers_2[i])):
     #   tree2.insert(numbers_2[i])
    print(f"Original List: {numbers}")
    print(f"In Order: {tree.in_order_traversal()}")
    print(f"Pre Order: {tree.pre_order_traversal()}")
    print(f"Post Order: {tree.post_order_traversal()}")
 
