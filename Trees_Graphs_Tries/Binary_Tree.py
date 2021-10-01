

class Binary_Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



    def in_order(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements

def insert(temp, data):

    if temp is None:
        root = Binary_Tree(data)
        return
        
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Binary_Tree(data)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Binary_Tree(data)
            break
        else:
            q.append(temp.right)

if __name__ == "__main__":

    root = Binary_Tree(10)  
    root.left = Binary_Tree(11)  
    root.left.left = Binary_Tree(7)  
    root.right = Binary_Tree(9)  
    root.right.left = Binary_Tree(15)  
    root.right.right = Binary_Tree(8)  
  
    print(f"Inorder traversal before insertion: {root.in_order()}") 
    
  
    key = 12
    insert(root, key)  
  
    print()  
    print(f"Inorder traversal after insertion: {root.in_order()}") 
    



