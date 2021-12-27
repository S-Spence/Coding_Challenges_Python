"""
 Binary Search Tree One-Class Implementation w DFS and BFS

"""

class BST:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.data = value

       

    def insert(self, val):
        """Insert a node into the BST"""
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BST(val)
        elif val > self.data:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BST(val)
        else:
            print("Value already in tree")
            
            
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
    
    
    def pre_order_traversal(self):
        """Pre-order traversal recusively traverses the tree by root, left, right (DFS algorithm)"""
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements

    def post_order_traversal(self):
        """Post-order traversal recusively traverses the tree by left, right, root. This method is good for deletion"""
        elements = []

        if self.left:
            # += instead of append copies all elements of right side list into left side list instead of .append() for one val
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        
        return elements
    
    def breadth_first_search(self):
        """Breadth-First Search, aka Level-Order"""
        # Create an empty queue for level order traversal
        queue = []
        # Enqueue Root 
        queue.append(self)
        # Create an empty list for output
        output = []

        while(len(queue) > 0):
            # Add front of queue to output and remove it from queue
            output.append(queue[0].data)
            node = queue.pop(0)
            # Skip if node is empty
            if node is None:
                continue
            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
 
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
        return output


if __name__ == "__main__":
    
    numbers = [3, 5, 2, 14, 6, 7]
    tree = BST(numbers[0])

    for i in range(1, len(numbers)):
        tree.insert(numbers[i])
    
    # Print traversals
    print(f"Original List: {numbers}")
    print(f"In Order: {tree.in_order_traversal()}")
    print(f"Pre Order: {tree.pre_order_traversal()}")
    print(f"Post Order: {tree.post_order_traversal()}")
    print(f"BFS: {tree.breadth_first_search()}")
 