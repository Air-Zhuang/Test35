'''
如何在环状数据结构中管理内存:弱引用weakref
(处理循环引用，进行垃圾回收)
'''
import weakref

class A:
    def __del__(self):
        print('in__del__')
a=A()
a2=weakref.ref(a)
a3=a2()
print(a3 is a)
del a
del a3
a2()
print(a2() is None)
print()
'''----------------------------------------------------------------------------------'''
class Data:
    def __init__(self,value,owner):
        self.owner=weakref.ref(owner) #使用弱引用，这样不会增加Node的引用计数
        self.value=value
    def __str__(self):
        return "%s's data,value is %s" % (self.owner(),self.value)
    def __del__(self):
        print('in Data.__del__')
class Node:
    def __init__(self,value):
        self.data=Data(value,self)
    def __del__(self):
        print('in Node.__del__')

node=Node(100)
del node    #删除引用成功
print()

'''----------------------------------------------------------------------------------'''
class Node:
    def __init__(self, data):
        self.data = data
        self._left = None
        self.right = None
    def add_right(self, node):
        self.right = node
        node._left = weakref.ref(self)
    @property
    def left(self):
        return self._left()
    def __str__(self):
        return 'Node:<%s>' % self.data
    def __del__(self):
        print('in __del__: delete %s' % self)

def create_linklist(n):
    head = current = Node(1)
    for i in range(2, n + 1):
        node = Node(i)
        current.add_right(node)
        current = node
    return head

head = create_linklist(1000)
print(head.right, head.right.left)
input()
head = None
