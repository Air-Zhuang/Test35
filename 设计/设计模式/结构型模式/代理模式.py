"""
把一个对象的操作代理到另一个对象
"""

from collections import deque

class Stack:
    def __init__(self):
        self.deque=deque()   #或者用list

    def push(self,value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()