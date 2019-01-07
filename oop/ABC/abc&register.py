import abc
import random

'''Alex Martelli的警告：不要自己定义抽象基类，除非你要构建允许用户拓展的框架——然而大多数情况下并非如此。
    日常使用中，我们与抽象基类的联系应该是创建现有抽象基类的子类，或者使用现有的抽象基类注册'''
class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self,iterable):
        """从可迭代对象中添加元素"""
    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回
            如果实例为空，这和方法应该抛出LookupError"""
    def loaded(self):
        """如果至少有一个元素，返回'True',否则返回'False'"""
        return bool(self.inspect())
    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items=[]
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

'''会报错：TypeError: Can't instantiate abstract class Fake with abstract methods load
    因为Fake没有实现load()抽象方法'''
# class Fake(Tombola):
#     def pick(self):
#         return 13
# Fake
# f=Fake()

'''Tombola抽象基类的子类1'''
class BingoCage(Tombola):
    def __init__(self,items):
        self._randomizer=random.SystemRandom()
        self._item=[]
        self.load(items)
    def load(self,items):
        self._item.extend(items)
        self._randomizer.shuffle(self._item)
    def pick(self):
        try:
            return self._item.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        self.pick()
b=BingoCage([1,2,3,4,5])
b.load([2,3,4,5,6,7])
print(b.pick())
print(b.loaded())   #继承了父类的loaded()和inspect()方法
print()

'''Tombola抽象基类的子类2'''
class LotteryBlower(Tombola):
    def __init__(self,iterable):    # list(iterable)会创建参数的副本，这依然是好的做法，因为我们要从中删除元素，而客户可能不希望自己提供的列表被修改
        self._balls=list(iterable)
    def load(self,iterable):
        self._balls.extend(iterable)
    def pick(self):
        try:
            position=random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        return self._balls.pop(position)
    def loaded(self):
        return bool(self._balls)
    def inspect(self):
        return tuple(sorted(self._balls))
l=LotteryBlower([1,2,3,4])
l.load([5,6,7,8])
print(l.pick())
print(l.loaded())
print(l.inspect())
print()

'''Tombola的虚拟子类'''
'''使用register方法声明虚拟子类'''
'''虚拟子类不会继承注册的抽象基类，而且任何时候都不会检查它是否符合抽象基类的接口，
    即便在实例化时也不会检查。为了避免运行时错误，虚拟子类要实现所需的全部方法。'''
from random import randrange

@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position=randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')
    load=list.extend
    def loaded(self):
        return bool(self)
    def inspect(self):
        return tuple(sorted(self))
t=TomboList([1,2,3,4])
t.load([5,6,7,8])
print(t.pick())
print(t.loaded())
print(t.inspect())
print(issubclass(TomboList,Tombola))
print(isinstance(t,Tombola))
print()



























