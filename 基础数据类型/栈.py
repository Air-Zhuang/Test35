"""
利用双端队列实现一个栈
"""

from collections import deque

class Stack:
    def __init__(self):
        self.deque=deque()   #或者用list

    def push(self,value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()