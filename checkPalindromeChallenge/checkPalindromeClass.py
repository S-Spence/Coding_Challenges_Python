#!/usr/bin/python
#-----------------------------------------------------------------------------------------------------------------------------------------
# Author: Sarah Spence
# Date: 2021-02-05
# Title: Check Palindrome
# Description: This class stores methods to check if a string is a palindrome. The methods store the string in both a stack and a queue.
#              The second two methods pop the stack and dequeue the queue to compare the strong forward and backward.
#----------------------------------------------------------------------------------------------------------------------------------------
from collections import deque

class checkPalindrome:
 
    # Class constructor, empty stack and queue
    def __init__(self):
        self.queue = deque()
        self.stack = []

    # Push character to stack
    def pushCharacter(self, char):
        self.stack.append(char)
    
    # Enqueue character in queue
    def enqueueCharacter(self, char):
        self.queue.append(char)
    
    # Pop character from top of stack
    def popCharacter(self):
        char = self.stack.pop()
        return char
    
    # Return first character in queue
    def dequeueCharacter(self):
        char = self.queue.popleft()
        return char
