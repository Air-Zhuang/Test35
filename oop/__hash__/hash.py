'''不可散列，意味着值可变在set([11,22,33])是ok的，在set([11,22,[33,44]])不ok
    因为列表里的元素包含列表是可变的，无法进行hash操作
    可散列：意味着值不可变并可进行hash操作'''

class Vector2d(object):
    typecode='d'
    def __init__(self,x,y):
        self._x=float(x)
        self._y=float(y)
    @property   #property函数用作装饰器可以创建只读属性
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    def __iter__(self):
        return (i for i in (self.x,self.y))
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
v1=Vector2d(3,4)
print(v1.x,v1.y)
# v1.x=7    #讲x设为只读，所以这里不可以改变x的值
v2=Vector2d(3.1,4.2)

print(hash(v1),hash(v2))    #实现了__hash__之后，向量变成可散列的了
print(set([v1,v2]))         #实现了__hash__之后，向量变成可散列的了