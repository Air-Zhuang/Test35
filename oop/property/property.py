'''如果 c 是 C 的实例化, c.x 将触发 getter,c.x = value 将触发 setter ， del c.x 触发 deleter。'''
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

'''将 property 函数用作装饰器可以很方便的创建只读属性：'''
'''上面的代码将 voltage() 方法转化成同名只读属性的 getter 方法。'''
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

'''property 的 getter,setter 和 deleter 方法同样可以用作装饰器：'''
'''这个代码和第一个例子完全相同，但要注意这些额外函数的名字和 property 下的一样，例如这里的 x。'''
class Parrot2:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x