'''用list实现一个定长的队列'''

import json

class Queue:
    def __init__(self,maxlen):
        self.q=[]
        self.maxlen=maxlen

    def append(self,value):
        if len(self.q)<self.maxlen:
            self.q.append(value)
        else:
            self.q.append(value)
            del self.q[0]

    def pop(self):
        value=self.q[-1]
        del self.q[-1]
        return value

    def empty(self):
        return 1 if len(self.q) else 0

    def __str__(self):
        return json.dumps(self.q)

q=Queue(2)
print(q.empty())
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
print(q.pop())
print(q)
print(q.empty())
print()
print()

"""
用两个栈实现一个队列
https://leetcode.com/problems/implement-queue-using-stacks/
"""
from collections import deque

class Stack:
    def __init__(self):     #先实现一个栈结构
        self.items=deque()
    def push(self,val):
        return self.items.append(val)
    def pop(self):          #删除并返回栈顶值
        return self.items.pop()
    def top(self):          #返回栈顶值
        return self.items[-1]
    def empty(self):
        return len(self.items)==0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1=Stack()
        self.s2=Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.删除队头元素
        """
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val=self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.返回队头元素
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            val=self.s1.pop()
            self.s2.push(val)
        return self.s2.top()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.empty())