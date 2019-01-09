'''
当看到一只鸟走起来像鸭子，游泳起来像鸭子，叫起来也像鸭子，那么这只鸟就可以被称为鸭子
'''
'''三个类都实现了共同的方法，方法名一样，这三个类就归为一种类型'''
'''java中实现多态要继承共同的父类，python实现多态只需要实现共同的方法名就可以'''
class Cat:
    def say(self):
        print("I am a cat")

class Dog:
    def say(self):
        print("I am a dog")

class Duck:
    def say(self):
        print("I am a duck")

animal_list=[Cat,Dog,Duck]
for i in animal_list:
    i().say()