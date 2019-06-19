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