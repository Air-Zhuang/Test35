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