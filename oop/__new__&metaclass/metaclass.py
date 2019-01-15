'''元类就是创建类的类，type就是元类'''

'''
用函数动态创建类(不常用)
'''
def create_class(name):
    if name=="user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name=="company":
        class Company:
            def __str__(self):
                return "company"
        return Company

MyClass=create_class("company")
my=MyClass()
print(my)
print()

'''
用type动态创建类(不常用)
type:
第一个参数：类名
第二个参数：继承元祖  如果什么都不继承则写()
第三个参数：类属性、类方法组成的字典
'''
class BaseClass:
    def answer(self):
        return "I am base"
def say(self):
    return "My name is "+self.name
Emp=type("Emp",(BaseClass,),{"name":"air","say":say})

emp=Emp()
print(emp.name)
print(emp.say())
print(emp.answer())
print()

'''真正的元类编程'''
class MetaClass(type):  #继承了type，就是一个元类
    def __new__(cls, *args, **kwargs):
        print("六道仙人创造了你")
        args[2]["title"]="title"        #args的第三个参数是存放属性值的
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "My name is " + self.name
class User2(metaclass=MetaClass):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "My name is " + self.name

user=User("air100%")
print(user)
print(user.title)
user2=User2("air200%")
print(user2)
print(user2.title)



