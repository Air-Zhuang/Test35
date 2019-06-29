"""
适配器模式
把不同对象的接口适配到同一个接口
想象一个多功能充电头，可以给不同的电器充电，充当了适配器
当我们需要给不同的对象统一接口的时候可以使用适配器模式
"""

class Dog:
    def __init__(self):
        self.name="Dog"
    def bark(self):
        return "woof!"

class Cat:
    def __init__(self):
        self.name="Cat"

    def meow(self):
        return "meow!"

class Adapter:
    def __init__(self,obj,**adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj=obj
        self.__dict__.update(adapted_methods)
    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj,attr)

objects=[]
dog=Dog()
objects.append(Adapter(dog,make_noise=dog.bark))
cat=Cat()
objects.append(Adapter(cat,make_noise=cat.meow))
for obj in objects:
    print("A {0} goes {1}".format(obj.name,obj.make_noise()))