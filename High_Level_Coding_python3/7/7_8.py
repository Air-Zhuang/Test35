'''
如何通过方法名字的字符串调用方法
'''

class Triangle:
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
    def get_area(self):
        a,b,c=self.a,self.b,self.c
        p=(a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**0.5
class Rectangle:
    def __init__(self,a,b):
        self.a,self.b=a,b
    def getArea(self):
        return self.a*self.b
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return self.r**2**3.14159

from operator import methodcaller

def get_area(shape, method_name = ['area', 'get_area', 'getArea']):
    for name in method_name:
        if hasattr(shape, name):
            return methodcaller(name)(shape)
        # f = getattr(shape, name, None)
        # if f:
        #     return f()

shape1 = Circle(1)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(4, 6)

shape_list = [shape1, shape2, shape3]
# 获得面积列表
area_list = list(map(get_area, shape_list))
print(area_list)
print()

s='abc123'
print(s.find('123'))
print(getattr(s,'find')('123'))
print()

s='abc123abc456'
print(s.find('abc',3))
methodcaller('find','abc',3)
print(methodcaller('find','abc',3)(s))
