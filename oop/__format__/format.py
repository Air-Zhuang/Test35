#format()和str.format()
brl=1/2.43
print(brl)
print(format(brl,'0.4f'))   #f表示小数形式的float类型
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
print(format(42,'b'))       #b和x分别表示二进制和十六进制的int类型
print(format(2/3,'.2%'))    #  %表示百分数形式
print()

#格式规范微语言是可拓展的
#datetime模块中的类,它们的__format__方法使用的格式代码与strftime()函数一样
from datetime import datetime
now=datetime.now()
print(format(now,'%H:%M:%S'))
print("It's now {:%I:%M %p}".format(now))
print()

#实现__format__
from array import array
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
    def angle(self):    #计算角度
        return math.atan2(self.y,self.x)
    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith('p'):
            fmt_spec=fmt_spec[:-1]
            coords=(abs(self),self.angle())
            outer_fmt='<{},{}>'
        else:
            coords=self
            outer_fmt='({},{})'
        components=(format(c,fmt_spec) for c in coords)
        return outer_fmt.format(*components)

v1=Vector2d(3,4)
print(format(v1))       #如果类没有定义__format__方法，这条语句会从object继承的方法会返回str(my_object)
print(format(v1,'.2f')) #如果类没有定义__format__方法，这条以及下面的会报错，因为类不认识'.2f'
print(format(v1,'.3e'))
print(format(Vector2d(1,1),'p'))
print(format(Vector2d(1,1),'3ep'))
print(format(Vector2d(1,1),'0.5fp'))