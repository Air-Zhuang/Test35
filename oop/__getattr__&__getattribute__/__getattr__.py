'''_getattr__是python里的一个内建函数，可以很方便地动态返回一个属性；
当调用不存在的属性时，Python会试图调用__getattr__(self,'key')来获取属性，并且返回key；'''

#example 1
class Student:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            return "这个属性在类中不存在，默认返回"
x = Student()
print(x.age)  # 40
print(x.name)  # error text omitted.....AttributeError, name
print()

#example 2
class A:
    def __init__(self,name,info={}):
        self.name=name
        self.info=info
    def __getattr__(self, item):
        return self.info[item]

a=A("air",{"age":23})
print(a.age)
print()

'''getattr_经典应用的例子，可以调用dict的键值对'''
class ObjectDict(dict):#只是例子，不建议继承dict
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value

od = ObjectDict(asf={'a': 1}, d=True)
print(od.asf, od.asf.a)     # {'a': 1} 1
print(od.d)                 # True
print()

'''getattr&setattr'''
class A:
    bar = 1

a = A()
print(getattr(a, 'bar'))          # 获取属性 bar 值
setattr(a, 'bar', 5)            # 设置属性 bar 值
print(a.bar)
