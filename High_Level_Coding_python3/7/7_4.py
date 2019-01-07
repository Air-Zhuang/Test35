'''如何创建可管理的对象属性'''

'''
在python中:property()方法整合了get方法，set方法
可管理的对象属性
'''

#使用property函数为类创建可管理属性

import math

class Circle(object):
    def __init__(self,radius):
        self.radius=radius
    def getRadius(self):
        return round(self.radius,2)
    def setRadius(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('wrong type.')
        self.radius=float(value)
    '''property函数用作装饰器的形式'''
    @property
    def S(self):
        return self.radius**2*math.pi
    @S.setter
    def S(self,s):
        self.radius=math.sqrt(s/math.pi)
    '''property(fget=None,fset=None,fdel=None,doc=None)'''
    R=property(getRadius,setRadius)     #整合set和get

c=Circle(3.2)
print(c.R) #相当于get
c.R=5.2   #相当于set
print(c.R)
print()
c.S=99.88
print(c.S)
print(c.R)