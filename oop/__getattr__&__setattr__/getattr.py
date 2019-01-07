'''_getattr__是python里的一个内建函数，可以很方便地动态返回一个属性；
当调用不存在的属性时，Python会试图调用__getattr__(self,'key')来获取属性，并且返回key；'''

class Student(object):
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            return "这个属性在类中不存在，默认返回"
x = Student()
print(x.age)  # 40
print(x.name)  # error text omitted.....AttributeError, name
print()

#_getattr_经典应用的例子，可以调用dict的键值对
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value

if __name__ == '__main__':
    od = ObjectDict(asf={'a': 1}, d=True)
    print(od.asf, od.asf.a)     # {'a': 1} 1
    print(od.d)                 # True
    print()


# >>>class A(object):
# ...     bar = 1
# ...
# >>> a = A()
# >>> getattr(a, 'bar')          # 获取属性 bar 值
# 1
# >>> setattr(a, 'bar', 5)       # 设置属性 bar 值
# >>> a.bar
# 5

class Dict(dict):
    '''
    通过使用__setattr__,__getattr__&__setattr__,__delattr__
    可以重写dict,使之通过“.”调用
    '''
    def __setattr__(self, key, value):
        print("In '__setattr__")
        self[key] = value
    def __getattr__(self, key):
        try:
            print("In '__getattr__&__setattr__")
            return self[key]
        except KeyError as k:
            return None
    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            return None
    def __call__(self, key):  # 带参数key的__call__方法
        try:
            print("In '__call__'")
            return self[key]
        except KeyError as k:
            return "In '__call__' error"
s = Dict()
print(s.__dict__)   # {}
s.name = "hello"  # 调用__setattr__# In '__setattr__
print(s.__dict__)  # 由于调用的'__setattr__', name属性没有加入实例属性字典中。# {}
print(s("name"))  # 调用__call__ # In '__call__' # hello
print(s.__dict__)
print(s["name"])  # dict默认行为    # hello
print(s.__dict__)
print(s.name)  # 调用__getattr__# In '__getattr__&__setattr__# hello

del s.name  # 调用__delattr__
print(s("name"))  # 调用__call__
# None