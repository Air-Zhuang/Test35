'''
__getattribute__ : 不管访问哪个属性，都返回__getattribute__返回的值
(尽量不要用)
'''
class A:
    def __init__(self,name,info={}):
        self.name=name
        self.info=info
    def __getattr__(self, item):
        return self.info[item]
    def __getattribute__(self, item):#尽量不要用__getattribute__
        return "Whatever you find,just me"

a=A("air",{"age":23})
print(a.name)
print(a.age)
print()