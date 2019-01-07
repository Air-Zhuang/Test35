'''@classmethod
    定义操作类，而不是操作实例的方法
    classmethod最常见的用途是定义备选构造方法'''

'''@staticmethod装饰器也会改变方法的调用方式，但是第一个参数不是特殊的值。
    其实，静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义'''

'''book:clasmethod装饰器非常有用，但是我从未见过不得不用staticmethod的情况
    如果想定义不需要与类交互的函数，那么在模块中定义就好了'''
class Demo(object):
    @classmethod
    def klassmeth(*args):   #按照约定，类方法的第一个参数名为cls(但是Python不介意具体怎么命名)
        return args
    @staticmethod
    def statmeth(*args):
        return args
    def normalmeth(self,*args):
        return args

print(Demo.klassmeth()) #可以直接用类名调用
print(Demo.klassmeth('spam'))
print(Demo.statmeth())  #可以直接用类名调用
print(Demo.statmeth('spam'))
d=Demo()
print(d.normalmeth())   #必须先实例化才能调用
print(d.normalmeth('spam'))
'''----------------------------------------------------------'''
from array import array
import math

class Vector2d:
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
    def __bytes__(self):
        return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
    @classmethod
    def frombytes(cls,octets):
        typecode=chr(octets[0])
        menv=memoryview(octets[1:]).cast(typecode)
        return cls(*menv)
    def __eq__(self, other):
        return tuple(self)==tuple(other)
    def __abs__(self):
        return math.hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))

v1=Vector2d(3,4)
for i in v1:    #__iter__
    print(i,"*"*9)
print(v1.x,v1.y)
x,y=v1          #定义了__iter__方法，才能拆包
print(x,y)
print(v1)
v1_clone=eval(repr(v1))
print(v1==v1_clone)
print(v1)
octets=bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1))
print(bool(Vector2d(0,0)))
print()

