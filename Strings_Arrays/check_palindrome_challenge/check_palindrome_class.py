#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-02-05
# Title: Check Palindrome
# Description: This class stores methods to check if a string is a palindrome. The methods store the string in both a stack and a queue.
#              The second two methods pop the stack and dequeue the queue to compare the strong forward and backward.
#----------------------------------------------------------------------------------------------------------------------------------------
from collections import deque

class CheckPalindrome:
 
    # Class constructor, empty stack and queue
    def __init__(self) -> None:
        self.queue = deque()
        self.stack = []

    # Push character to stack
    def push_character(self, char) -> str:
        self.stack.append(char)
    
    # Enqueue character in queue
    def enqueue_character(self, char) -> str:
        self.queue.append(char)
    
    # Pop character from top of stack
    def pop_character(self) -> str:
        char = self.stack.pop()
        return char
    
    # Return first character in queue
    def deque_character(self) -> str:
        char = self.queue.popleft()
        return char
