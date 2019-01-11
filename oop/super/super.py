'''
__init__方法遵循正常的继承
super().__init__()      调用父类的初始化方法，使用父类的参数
super().__init__(a,b)   调用父类的初始化方法，使用子类的参数
'''

'''==============================================='''
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")


b=B()       #不会自动调用父类的初始化方法
print()

class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
        super().__init__()


b=B()       #加上super之后调用父类的初始化方法
print()
'''==============================================='''
class A:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b

class B(A):
    def __init__(self,a,b):     #如果有子类有__init__方法而又没有调用super().__init__()，则不会自动调用父类的初始化方法
        # super().__init__(a=a+100,b=b+100)
        # super().__init__()
        pass
b=B(11,22)
# print(b.a)
'''==============================================='''
from threading import Thread


class MyThread(Thread):
    def __init__(self,name,user):
        self.user=user
        self.name=name

class MyThread2(Thread):
    def __init__(self,name,user):
        self.user=user
        super().__init__(name=name)     #在父类构造方法中的初始化参数无需在子类中重复初始化

'''==============================================='''
'''super的调用顺序实际是mro算法'''
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

d=D()
print(D.__mro__)