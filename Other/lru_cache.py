"""This is the doubly-linked list implementation. You can also use the func tools library and use the @lru_cache from import functools
This also runs in O(1) time with default max size of 128. You can change maxsize as a parameter.
 However, probably not what they want in an interview. 
https://leetcode.com/problems/lru-cache/submissions/"""

# Define node class
class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# LRU class
class LRUCache:
    
    def __init__(self, capacity: int):
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.capacity = capacity
        self.curr_size = 0
        self.node_dict = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        """Get a value from the cache"""
        # Return -1 if not in cache
        if key not in self.node_dict:
            return -1
        node = self.node_dict[key]
        
        if node:
            result = node.val
            self.delete(node)
            self.add(node)
        
        return result
        
        

    def put(self, key: int, value: int) -> None:
        """Put either adds or overrides a node"""
        if key in self.node_dict:
            node = self.node_dict[key]
            node.val = value
            self.delete(node)
            self.add(node)
        else:
            if self.curr_size >= self.capacity:
                lru_node = self.head.next
                self.node_dict.pop(lru_node.key)
                self.delete(lru_node)
                self.curr_size -= 1
            
            new_node = Node(key, value)
            self.node_dict[key] = new_node
            self.add(new_node)
            self.curr_size += 1
            
        
    def delete(self, node: Node) -> None:
        """Delete a node from the linked list"""
        next_node = node.next
        prev_node = node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node
        
    def add(self, node: Node) -> None:
        """Add a node to the head of the linked list"""
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node  
