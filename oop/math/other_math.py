'''
Fluent Python:
不能重载内置类型的运算符
不能新建运算符，只能重载现有的
某些运算符不能重载---is、and、or 和not(不过位运算符&、| 和 ~ 可以)
'''
import math
class Vector2d(object):
    typecode='d'
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def __iter__(self):
        return (i for i in (self.x,self.y))
        # yield self.x              #这样也可以
        # yield self.y
        # return (self.x,self.y)    #这样写不行
    def __repr__(self):
        class_name=type(self).__name__
        print("*self:", *self)
        print("self:", self)
        return '{}({!r},{!r})'.format(class_name,*self)
    def __str__(self):
        return str(tuple(self))
    def __eq__(self, other):
        return tuple(self)==tuple(other)
    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))
    def __neg__(self):
        return Vector2d(-x for x in self)
    def __pos__(self):
        return Vector2d(self)
    def __bool__(self):
        return bool(abs(self))