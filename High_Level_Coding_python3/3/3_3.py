'''
使用生成器函数实现可迭代对象：yield
'''
from collections import Iterable,Iterator

def f():
    print('in f(),1')
    yield 1
    print('in f(),2')
    yield 2
    print('in f(),3')
    yield 3
g=f()
print(isinstance(g,Iterable))
print(isinstance(g,Iterator))
print(iter(g) is g)
for i in f():
    print(i)
print()
'''------------------------------------------'''
class X(object):
    def __iter__(self):
        yield 1
        yield 2
        yield 3
x=X()
for i in x:
    print(i)
print()
'''------------------------------------------'''
class PrimeNumbers(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrime(self,k):
        if k<2:
            return False
        # for i in range(2,k):
        #     if k%i==0:
        #         return False
        # return True
        return all(map(lambda x : k % x,range(2,k)))

    def __iter__(self):
        for i in range(self.start,self.end):
            if self.isPrime(i):
                yield i

for i in PrimeNumbers(1,100):
    print(i,end=" ")