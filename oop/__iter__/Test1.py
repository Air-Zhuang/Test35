class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe=safe
        self.iter=iter(data)
    def __iter__(self):
        return self
    def __next__(self,howmany=1):
        retval=[]
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval
a=AnyIter(range(10))
i=iter(a)
for j in range(1,5):
    print(j,":",i.__next__(j))


class MyIter(object):
    def __init__(self,some):
        self.iter=iter(some)
    def __iter__(self):
        return self
    def __next__(self):
        return [self.iter.__next__()]

it=iter(MyIter(range(10)))
for i in it:
    print(i)

class Vector:
    def __init__(self,lst):
        self._values=list(lst)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        return Vector([a+b for a,b in zip(self,another)])

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))
u=Vector([5,2])
u2=Vector([3,4])
print()
print(u+u2)