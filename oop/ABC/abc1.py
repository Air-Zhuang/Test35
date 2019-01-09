from abc import ABC, abstractmethod     #注意这里是abc模块下的ABC,不是collections模块下的abc

'''
类似于java中的抽象接口,只要继承的父类有抽象方法,必须实现(尽量不要使用,可以用python的鸭子类型来代替)
1、我们需要强制某个子类必须实现某些方法
2、我们某些情况下希望判定某个对象的类型
'''

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

'''1、我们需要强制某个子类必须实现某些方法'''
class A(ABC):
    @abstractmethod
    def ppp(self):
        pass
class B(A):
    def ppp(self):
        print("This is B")      #子类必须实现父类的抽象方法
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
print()

class A:
    def ppp(self):
        raise NotImplementedError    #可以用Python的鸭子类型代替抽象基类的实现
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
print()

'''2、我们某些情况下希望判定某个对象的类型'''
from collections.abc import Sized

class Company:
    def __init__(self,employee_list):
        self.employee=employee_list
    def __len__(self):
        return len(self.employee)

com=Company(["air1","air2"])
print(hasattr(com,"__len__"))   #传统判定
print(isinstance(com,Sized))    #通过抽象基类判定