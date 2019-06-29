"""
修改类的属性名称为小写
"""
class LowercaseMeta(type):
    def __new__(cls,name,bases,attrs):
        lower_attrs={}
        for k,v in attrs.items():
            if not k.startswith("__"):      #排除魔术方法
                lower_attrs[k.lower()]=v
            else:
                lower_attrs[k]=v
        return type.__new__(cls,name,bases,lower_attrs)

class LowercaseClass(metaclass=LowercaseMeta):
    BAR=True

    def HELLO(self):
        print("hello")

print(dir(LowercaseClass))