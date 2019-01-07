'''
让类支持比较操作
__lt__小于,__le__小于等于,__gt__大于,__ge__大于等于,__eq__等于,__ne__不等于
'''
'''声明抽象类方法的推荐方法是:
    class MyABC(abc.ABC):
        @classmethod
        @abstractmethod
        def an_abstract_classmethod(cls, ...):
            pass    
'''
from functools import total_ordering
from abc import ABC,abstractmethod,ABCMeta #导入抽象基类工具

#使用标准库下的functools下的类装饰器total_ordering可以简化此过程

@total_ordering
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def __lt__(self,other):         #使用@total_ordering只需定义小于和等于两个，剩下的可以自动推测出来
        print('in __lt__')
        if not isinstance(other,Shape):
            raise TypeError('other is not Shape')
        return self.area()<other.area()
    def __eq__(self, other):
        print('in __eq__')
        if not isinstance(other,Shape):
            raise TypeError('other is not Shape')
        return self.area()==other.area()

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w * self.h
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2*3.14

r1=Rectangle(5,3)
r2=Rectangle(4,4)
c1=Circle(3)

print(c1<=r1)
print()
print(r1>c1)
print()
print(c1>=r1)
print()
print(r1<c1)

