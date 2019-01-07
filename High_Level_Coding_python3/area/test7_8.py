# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 23:23'

from High_Level_Coding_python3.area.lib1 import Circle
from High_Level_Coding_python3.area.lib2 import Triangle
from High_Level_Coding_python3.area.lib3 import Rectangle

from operator import methodcaller

def getArea(shape):
    #第一种方式：getattr()
    for name in ('area','getArea','get_area'):
        f=getattr(shape,name,None)
        if f:
            return f()

shape1=Circle(2)
shape2=Triangle(3,4,5)
shape3=Rectangle(6,4)

shapes=[shape1,shape2,shape3]
print(map(getArea,shapes))

#第二种方式methodcaller
'''
实际上methodcaller等价于下面的函数：

def methodcaller(name, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)
    return caller

可以看到，它的实质还是使用getattr函数，只不过它把它封装起来了，调用方式不同了。
我认为7-8这节不能使用methodcaller解决问题。
'''