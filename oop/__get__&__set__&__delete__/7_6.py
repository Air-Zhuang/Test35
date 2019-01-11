'''
属性描述符
使用描述符对实例属性做类型检查(类似sqlalchemy中对表字段做数据类型检查)
'''
#原理
class Descriptor:
    def __init__(self,key):
        self.key=key
    def __set__(self, instance, value):
        print('in__set__')
        # instance.__dict__[self.key]=value     #实际是从__dict__中取
        self.key=value
    def __get__(self, instance, cls):
        print('in__get__',instance,cls)
        # return instance.__dict__[self.key]
        return self.key
    def __delete__(self, instance):
        print('in__del__',instance)
        # del instance.__dict__[self.key]
        del self.key

d=Descriptor('xxx')    #Descriptor直接创建属性
print(d.__dict__)
print()

class A:
    x=Descriptor('x')
    y=Descriptor('y')
a=A()
a.x=5
a.y=6
print(a.x)
print(a.y)
print()

#example 1
class Attr:
    def __init__(self,name,type_):
        self.name=name
        self.type_=type_
    def __get__(self, instance, cls):
        # return instance.__dict__[self.name]   #使传进来的属性可以变成Person的类属性
        return self.name
    def __set__(self, instance, value):
        if not isinstance(value,self.type_):
            raise TypeError('expected an %s' % self.type_)
        # instance.__dict__[self.name]=value  #使传进来的属性可以变成Person的类属性
        self.name=value
    def __delete__(self, instance):
        # del instance.__dict__[self.name]
        del self.name

class Person:
    name=Attr('name',str)
    age=Attr('age',int)

p=Person()
p.name='Bob'
print(p.name)
# p.age='17'    #这里会抛出类型不匹配的异常
print()

#example 2  (实现类似sqlalchemy的属性检查)
class IntField:
    def __init__(self,name):
        self.name=name
    def __get__(self, instance, cls):
        # return instance.__dict__[self.name]
        return self.name
    def __set__(self, instance, value):
        if not isinstance(value,int):
            raise TypeError("not a int proprety")
        # instance.__dict__[self.name]=value
        self.name=value
    def __delete__(self, instance):
        # del instance.__dict__[self.name]
        del self.name
class User:
    age=IntField("age")
    year=IntField("year")

user=User()
user.age=23
user.year=1995
print(user.age)
print(user.year)
# user.year="1995"      #抛出TypeError