"""
迭代器模式
Python内置对迭代器模式的支持
比如我们可以用for遍历各种Iterable的数据类型
Python里可以实现__next__和__iter__实现迭代器
"""

from collections import deque

class Stack:
    def __init__(self):
        self.deque=deque()   #或者用list

    def push(self,value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __iter__(self):
        res=[]
        for i in self.deque:
            res.append(i)
        for i in reversed(res):
            yield i

s=Stack()
s.push(1)
s.push(2)
s.push(3)
for i in s:
    print(i)