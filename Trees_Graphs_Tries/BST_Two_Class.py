"""
Binary Search Tree Two-Class Implementation W/ BFS and DFS.

"""


class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # --------------------------------------------------------------
    # Class methods to insert
    # --------------------------------------------------------------
    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self._insert(val, self.root)

    def _insert(self, value, current):
        """Private method to handle insert logic"""

        if value < current.value:
            # Insert right side
            if current.left == None:
                current.left = TreeNode(value)
            else:
                self._insert(value, current.left)

        elif value > current.value:
            if current.right == None:
                current.right = TreeNode(value)
            else:
                self._insert(value, current.right)
        else:
            print("The value is already in the tree.")

    # --------------------------------------------------------------------
    # Breadth first search
    # --------------------------------------------------------------------

    def breadth_first_search(self) -> "list[int]":
        """Return a list of values using breadth first search"""
        # Create an empty queue for level order traversal
        queue = []
        # Create a list to store the output
        values = []
        # Enqueue Root
        queue.append(self.root)

        while(len(queue) > 0):
            # Append the current value to values list and set the node the the current value
            node = queue.pop(0)
            values.append(node.value)

            if node is None:
                continue
            # Enqueue left child
            if node.left:
                queue.append(node.left)

            # Enqueue right child
            if node.right:
                queue.append(node.right)
        return values

    # --------------------------------------------------------------------------------
    # Methods for Depth First Search: In-Order, Post-Order, Pre-Order
    # --------------------------------------------------------------------------------

    # ------------------------
    # In-Order
    # ------------------------
    def in_order(self) -> "list[int]":
        """In-Order: Left, Node, Right"""
        values = []
        if self.root != None:
            self._in_order(values, self.root)
        return values

    def _in_order(self, values: "list[int]", current: TreeNode):
        """Private method to fill the list of values using in-order traversal"""
        if current != None:
            if current.left:
                self._in_order(values, current.left)
            values.append(current.value)
            if current.right:
                self._in_order(values, current.right)

    # -----------------------
    # Pre-Order
    # -----------------------
    def pre_order(self) -> "list[int]":
        """Pre-Order traversal: Node, Left, Right"""
        values = []
        if self.root != None:
            self._pre_order(values, self.root)
        return values

    def _pre_order(self, values: "list[int]", current: TreeNode):
        """Private method to fill the list of values using pre-order traversal"""
        if current != None:
            values.append(current.value)
            if current.left:
                self._pre_order(values, current.left)
            if current.right:
                self._pre_order(values, current.right)

    # -------------------------
    # Post-Order
    # -------------------------
    def post_order(self) -> "list[int]":
        """Post-Order Traversal: Left, Right, Node"""
        values = []
        if self.root != None:
            self._post_order(values, self.root)
        return values

    def _post_order(self, values: "list[int]", current: TreeNode):
        """Private method to fill the list of values using post-order traversal"""
        if current != None:
            if current.left:
                self._post_order(values, current.left)
            if current.right:
                self._post_order(values, current.right)
            values.append(current.value)


if __name__ == "__main__":
    bst_1 = BST()

    bst_1.insert(5)
    bst_1.insert(4)
    bst_1.insert(6)
    bst_1.insert(7)
    bst_1.insert(3)

    print(f"In-Order Traversal: {bst_1.in_order()}")
    print(f"Pre-Order Traversal: {bst_1.pre_order()}")
    print(f"Post-Order Traversal: {bst_1.post_order()}")
    print(f"Breadth First Search: {bst_1.breadth_first_search()}")
