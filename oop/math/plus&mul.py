class NumStr(object):
    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[%d::%r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return NumStr(self.__num + other.__num, self.__string + other.__string)     #两种语法一样
            # return self.__class__(self.__num + other.__num, self.__string + other.__string)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return NumStr(self.__num * other, self.__string * other)
            # return self.__class__(self.__num * other, self.__string * other)          #两种语法一样
        else:
            raise TypeError


a = NumStr(1, "aa")
b = NumStr(2, "bb")
c = NumStr(3, "cc")
print(a + b + c)
print(c * 3)

class A:
    def __init__(self,l):
        self.l=l
    def __mul__(self, other):
        return A([i*other for i in self.l])
    def __rmul__(self, other):
        return A([i*other for i in self.l])
    def __str__(self):
        return "%s" % self.l


a=A([1,2,3])

print(a*2)  #__mul__
print(2*a)  #__rmul__

