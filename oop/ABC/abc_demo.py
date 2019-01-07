from abc import ABC, abstractmethod

'''类似于java中的抽象接口'''

'''abc.ABC是Python3.4新增的类。
    从python3.0到3.3,必须在class语句中使用metaclass=ABCMeta:  class Tombola(metaclass=ABCMeta):
    python2:  class Tombola(object):
                    __metaclass__=abc.ABCMeta
'''
'''声明抽象类方法的推荐方法是:
    class MyABC(abc.ABC):
        @classmethod
        @abstractmethod
        def an_abstract_classmethod(cls, ...):
            pass    
'''
class A(ABC):
    @abstractmethod
    def ppp(self):
        pass
class B(A):
    def ppp(self):
        print("This is B")
class C(A):
    def fool(self):
        print("I'm fool!")
    def ppp(self):
        print("This is C")
b = B()
b.ppp()
c = C()
c.fool()
c.ppp()