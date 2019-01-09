'''
让类支持比较操作
__lt__小于,__le__小于等于,__gt__大于,__ge__大于等于,__eq__等于,__ne__不等于
'''

from functools import total_ordering
from abc import abstractmethod,ABCMeta #导入抽象基类工具

#使用标准库下的functools下的类装饰器total_ordering可以简化此过程

# @total_ordering
# class Shape(metaclass=ABCMeta):   #从python3.0到3.3,必须在class语句中使用metaclass=ABCMeta
#     def area(self):
#         pass

@total_ordering
class Shape(object):
    @abstractmethod
    def area(self):                 #第二种方式：创建抽象接口
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
        return self.w * self.h      #子类必须实现父类的抽象方法
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2*3.14

r1=Rectangle(5,3)
r2=Rectangle(4,4)
c1=Circle(3)

print(c1<=r1)
print(r1>c1)

