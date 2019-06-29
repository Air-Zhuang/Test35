"""
单例模式：一个类只能创建同一个对象
Python的模块其实就是单例的，只会导入一次
"""
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            _instance=super().__new__(cls,*args,**kwargs)
            cls._instance=_instance
        return cls._instance

class MyClass(Singleton):
    pass

c1=MyClass()
c2=MyClass()

print(id(c1))
print(id(c2))
print(c1 is c2)