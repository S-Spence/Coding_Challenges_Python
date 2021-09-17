import random

class BST:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
        self.size = 0

    def insert(self, val):
        # If the tree is empty, set the current node as the root node
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


    """In order traversal recursivly traverses the tree by left, root, right. In order prints BST in sorted order"""
    def in_order_traversal(self):
        elements = []
        if self.left:
            # += instead of append copies all elements of right side list into left side list instead of .append() for one val
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    """Pre-order traversal recusively traverses the tree by root, left, right"""
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





if __name__ == "__main__":
    numbers = [5, 6, 4, 3, 2, 56, 45, 32, 17, 89, 92, 50]
    print(numbers)
    tree = BST(numbers[0])

    for i in range(1, len(numbers)):
        tree.insert(numbers[i])

    print(tree.in_order_traversal())
    print(tree.pre_order_traversal())




