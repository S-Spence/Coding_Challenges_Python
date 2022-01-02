"""
Problem: Implement a priority queue.
      Can use max or min heap. This implementation uses max.

Note: A max heap is a complete binary tree where every child node is less than its parent. The root node is always
      the greatest element in the tree.
      A min tree is also a complete binary tree where every child node is greater than its parent. The root node
      is always the lowest value.

      When storing the heap in an array, the following formulas locate nodes
            - parent = ((arr_index-1)//2)
            - left = (arr_index * 2) + 1
            - right = (arr_index * 2) + 2

      When we remove or retrieve from a max heap, we only want to return the greatest value, which will be the root node. 
      Then, we must restructure the heap to ensure it is still in the correct order and still a complete binary tree.
      When removing, first you take the root node out, then move the right-most element of the bottom row into the root node place. 
      This step maintains the complete binary tree.
      Next, you check the values and swap the node into the correct place.

"""


class PriorityQueue:

    def __init__(self, _heap=[]):
        self._heap = _heap

    # Private methods
    def _compare_max_heap(self, index_1: int, index_2: int) -> bool:
        """Private method to compare valus for max heap"""
        return self._heap[index_1] > self._heap[index_2]

    def _parent(self, index: int) -> int:
        """Private method to return index of the parent node"""
        return (index-1)//2

    def _left(self, index: int) -> int:
        """Private method to return the index of the left ndoe"""
        return (index * 2) + 1

    def _right(self, index: int) -> int:
        """Private method to return the index of the right node"""
        return (index * 2) + 2

    def _swap(self, index_1: int, index_2: int):
        """Private method to swap heap elements"""
        temp = self._heap[index_1]
        self._heap[index_1] = self._heap[index_2]
        self._heap[index_2] = temp

    def _sift_up(self):
        """A method to continuously swap elements with the parent until they cannot be swapped anymore. Time: O(logn)"""
        # Initialize the node index to the last element
        node_index = self.size()-1

        # while the node index is in range and the node at the index is greater than its parent, swap elements.
        while node_index > 0 and self._compare_max_heap(node_index, self._parent(node_index)):
            # swap elements
            self._swap(node_index, self._parent(node_index))
            # shift node index
            node_index = self._parent(node_index)

    def _sift_down(self):
        """Private method to reorder the heap after removing an element. Time: O(logn)"""
        node_index = 0
        # while there is a left child or a right child, and the right child or the left child is out of place
        while ((self._left(node_index) < self.size() and self._compare_max_heap(self._left(node_index), node_index)) or
               (self._right(node_index) < self.size() and self._compare_max_heap(self._right(node_index), node_index))):

            # set the greater index to right if the right child exists and is greater than left child, else left
            if self._right(node_index) < self.size() and self._compare_max_heap(self._right(node_index), self._left(node_index)):
                greater_index = self._right(node_index)
            else:
                greater_index = self._left(node_index)
            # Swap the elements
            self._swap(greater_index, node_index)
            # Update node index
            node_index = greater_index

    # Public methods
    def is_empty(self):
        """Determine if the queue is empty"""
        return self.size() == 0

    def size(self):
        """Return the size of the queue"""
        return len(self._heap)

    def peek(self):
        """Return the priority element of the queue. No removal."""
        return self._heap[0]

    def push(self, val: int):
        """Add an element to the priority queue"""
        self._heap.append(val)
        self._sift_up()
        return self.size()

    def pop(self):
        """Remove the priority element from the queue"""
        # swap the first and last elements so you can pop from the end without shifting the array
        if self.size() > 1:
            self._swap(0, self.size()-1)
        # Now, pop the end value because you just swapped it for the priority element
        value = self._heap.pop()
        # Rearrange queue to correct order
        self._sift_down()
        return value


test = [50, 40, 25, 20, 10, 15]

pq = PriorityQueue(test)

pq.push(5)

print(pq._heap)

pq.pop()

print(pq._heap)
