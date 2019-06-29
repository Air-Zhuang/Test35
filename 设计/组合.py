from collections import deque

class Stack:
    def __init__(self):
        """
        使用组合的设计方式，将对Stack的操作转换成对内部deque的操作
        """
        self._deque=deque

    def push(self,value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque)==0