# -*- coding: UTF-8 -*-

class MyIter(object):
    def __init__(self,some):
        self.iter=iter(some)
    def __iter__(self):
        return self
    def __next__(self):
        return [self.iter.__next__()]

if __name__ == '__main__':
    it=iter(MyIter(range(10)))
    for i in it:
        print(i)

